# Ownership — who owns what, so nothing clashes

Set on 25 Sep 2026 after two chats built overlapping CRM packages. One job = one chat = one repo (or one branch in a repo), and every chat reads the Project docs before building.

| Thing | Owner | Repo | Notes |
|---|---|---|---|
| The feed: editions, desk cards, verification, corrections | Newsroom (Daily Brief writer task + the Newsroom chat) | Newsroom page + Research Supabase project (`newsroom_editions`, edge function `newsroom-file`) | Surface 1. The swarm reads it, never writes it. |
| The public site: buytrigger.club, /join/ | Newsroom web build (Lisa) | `buytrigger-newsroom` | Surface 3 later. |
| The swarm: bee prompts, gates, tools, charts, ledger | Swarm chat | `buytrigger-swarm` (this repo) | Surface 2. Writes only the `journalism` collection and Typefully drafts. |
| Sending: review and publish the drafts | Marketing team | Typefully | The only humans who press send. |
| CRM Stage 1: counter, `crm-ingest`, `crm` schema, tagged-link registry | CRM chat | as the CRM chat's handover says (`claude/crm-stage1-handover.md`) | The swarm's duplicate package was withdrawn 25 Sep; only `utm_content` on post links is the swarm's. |
| The members' dashboard | Dashboard chats (e.g. 3.18) | `buytrigger-dashboard` | The swarm never touches it. |
| Research Department systems | Research chat | `BuyTrigger-Research` | Not recreated anywhere else. |
| Production Supabase (`brzawmbpwkdundruicca`) | Alex | — | Off limits for Newsroom and swarm tables. |
| Research Supabase (`paoxcmxteemakhyvwihn`) | Research / Newsroom | — | Where the "one source" move would put desk cards and the ledger (`schema/supabase/`). Needs Alex to run the SQL. |

## Decisions that are Alex's

Member access, entitlements, production data, deployment, anything that publishes to the public. The swarm makes none of these; it drafts and records.

## Before any chat builds something new

1. Read `Project/INDEX.md` and the docs in `Project/active/` (or `claude/` in the Project).
2. Search the Project for the job name. If a handover exists, that chat owns it.
3. Name the branch `<job>-<stage>` and say so in the first message.
