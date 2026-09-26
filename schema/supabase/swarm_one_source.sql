-- buytrigger-swarm · "one source" move · PROPOSAL, NOT YET RUN
--
-- Today the desk cards and the bees' ledger live in the Newsroom page's own
-- database (ArtifactData collections `desk` and `journalism`). That works, but
-- it is a second store beside the Research Supabase project, where the
-- editions already land (table newsroom_editions, via edge function
-- newsroom-file). This script moves the two swarm-side stores next to them,
-- so there is one place to query "what was filed, what was carded, what was
-- drafted, what was sent".
--
-- Target: the RESEARCH Supabase project (paoxcmxteemakhyvwihn), its own
-- schema `swarm`. Never the production project.
--
-- Alex runs this in the SQL Editor when he decides to. Nothing in the bees
-- depends on it yet; when it is live, the bee prompts change their
-- "Where things live" section and the Daily Brief writer's desk step would
-- need to file cards here as well (that prompt is the Newsroom's to change).
--
-- Safe to run twice. Ends with COMMIT.

begin;

create schema if not exists swarm;

-- Desk cards: one row per card, keyed by edition + card id.
create table if not exists swarm.cards (
  edition_id   text        not null,
  card_id      text        not null,
  rank         text,
  klass        text        not null,          -- EVERGREEN PACK | BREAKING POST | CLOSING RECAP | INTRADAY EXPLAINER
  title        text        not null,
  why          text,
  formats      text,
  "window"     text,
  life_s       integer,
  story        integer     not null,          -- index into the edition's stories[]
  created_at   timestamptz not null,
  expires_at   timestamptz generated always as (created_at + make_interval(secs => coalesce(life_s, 0))) stored,
  filed_at     timestamptz not null default now(),
  primary key (edition_id, card_id)
);

-- The ledger: one row per bee action. A card or a night can have at most one
-- drafted row; rejections are one row each.
create table if not exists swarm.ledger (
  id                 bigint generated always as identity primary key,
  layer              smallint    not null check (layer in (1, 2, 3)),
  day                date        not null,                  -- UK date of the run
  edition_id         text,                                  -- Layer 1: the card's edition
  card_id            text,                                  -- Layer 1: the card
  outcome            text        not null check (outcome in ('drafted', 'rejected', 'skipped')),
  reason             text,                                  -- rejected/skipped: the gate that failed
  typefully_draft_id bigint,
  angle              text,
  story              text,
  editions           text[],                                -- Layer 2/3: editions used
  score              integer,
  stock_named        boolean     not null default false,
  platforms          text[],
  charts             text[],
  charts_attached    text,
  fca                text,
  overlaps_l1        bigint,                                -- Layer 2: the Layer 1 draft on the same story, if any
  run_at             timestamptz not null,
  at                 timestamptz not null default now(),
  sent_at            timestamptz,                           -- filled later from Typefully when marketing sends
  sent_platforms     text[],
  note               text
);

create unique index if not exists ledger_one_draft_per_card
  on swarm.ledger (edition_id, card_id) where layer = 1 and outcome = 'drafted';
create unique index if not exists ledger_one_draft_per_night
  on swarm.ledger (day) where layer = 2 and outcome = 'drafted';
create unique index if not exists ledger_one_draft_per_week
  on swarm.ledger (day) where layer = 3 and outcome = 'drafted';
create index if not exists ledger_day on swarm.ledger (day, layer);

-- What was drafted and whether it went out: the weekly scoreboard's source.
create or replace view swarm.drafts_weekly as
select date_trunc('week', day)::date as week,
       layer,
       count(*) filter (where outcome = 'drafted')  as drafted,
       count(*) filter (where outcome = 'rejected') as rejected,
       count(*) filter (where sent_at is not null)  as sent
from swarm.ledger
group by 1, 2
order by 1 desc, 2;

-- Lock it down: only the service role (the bees' filing function, later) and
-- named admins read or write. No anon access.
alter table swarm.cards  enable row level security;
alter table swarm.ledger enable row level security;
revoke all on schema swarm from anon, authenticated;
revoke all on all tables in schema swarm from anon, authenticated;

commit;

-- After running: the bees would file through a small edge function
-- (swarm-file), the same pattern as newsroom-file, with a filing token kept
-- in the task prompt and never printed. That function is written when this
-- script is live, not before.
