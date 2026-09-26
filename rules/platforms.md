# Platform rules — what X, Threads and Substack accept

Learned the hard way on 24 Sep 2026, when four drafts were published through Typefully and two Threads posts and one X post failed. Since then: marketing sends, and every draft passes `tools/check_lengths.py` before it is created.

## X

- Each post ≤ 280 characters. Count with code; tighten, never truncate.
- **No URL and no bare domain anywhere in the thread** — not `buytrigger.club`, not `treasury.gov`. X refuses posts published through an app when they contain a link ("Direct publishing of X drafts containing URLs is blocked"). Name sources in words: "the US Treasury's daily table", "the company's Form 4 filing", "the Census Bureau release".
- The last post ends with: `Full edition, every source, on the BuyTrigger Newsroom.`
- If any post names a stock, by `$TICKER` or by company name as the subject, the thread carries a not-advice line. Layer 2 puts `Not advice, not a view on the stock.` in the last post before the closing line.
- Layer 1: 3–5 posts. Layer 2: 8–12 posts.
- Attribution: X posts cannot carry a tracked link, so X traffic is attributed by the bio link and the referrer.

## Threads

- Each post ≤ 450 characters. (Typefully allows 500; posts of 494 characters carrying arrows and em dashes failed on 24 Sep and Typefully gave no reason. The cause is unconfirmed; 450 and plain punctuation is the working rule until it is.)
- Plain punctuation only: full stops, commas, colons, question marks. No arrows, em dashes, en dashes, bullets, middle dots or other special symbols.
- The last post ends with the tracked link on its own line (see below). If a stock is named, `Not advice.` before the link.
- Layer 1: one post. Layer 2: 3–5 posts.

## Substack (Notes, via Typefully)

- Layer 2 only: one note of 1,000–1,800 characters. Not-advice framing when a stock is named, sources named in words, tracked link at the end.
- Layer 3 articles are not Typefully drafts; they are delivered as a Markdown file for Alex to paste into Substack himself.

## Tracked links

Every Threads and Substack post carries a link with `utm_content` set, so each post gets its own line in the CRM's `content_daily` view once CRM Stage 1 is live.

| Where | Link |
|---|---|
| Layer 1 Threads post | `buytrigger.club/?utm_source=threads&utm_medium=post&utm_campaign=newsroom&utm_content=<edition_id>-<card_id>` |
| Layer 2 Threads post | `https://buytrigger.club/?utm_source=threads&utm_medium=post&utm_campaign=newsroom&utm_content=l2-<date>` |
| Layer 2 Substack note | `https://buytrigger.club/?utm_source=substack&utm_medium=post&utm_campaign=newsroom&utm_content=l2-<date>` |
| X bio | `https://buytrigger.club/join/?utm_source=x&utm_medium=bio&utm_campaign=4-0-early-bird` |
| Threads bio | `https://buytrigger.club/join/?utm_source=threads&utm_medium=bio&utm_campaign=4-0-early-bird` |
| Substack letter | `https://buytrigger.club/join/?utm_source=substack&utm_medium=letter&utm_campaign=4-0-early-bird` |

The bio and letter links are the CRM chat's registry (`claude/crm-stage1-handover.md` in the Project). The swarm only adds `utm_content` to its own post links.

## Dating

Say "on Wednesday", "on 25 Sep", never "today", "tonight" or "yesterday". Marketing may send a draft the next day.

## Charts

- Drawn by code from claim rows (`charts/`). No image generation.
- Attached to the draft automatically once the upload host `typefully-user-uploads.s3.amazonaws.com` is on Claude's allowed domains. Until then the bee tries the upload once, then leaves the PNGs in the session's output files and says which chart goes on which post in the scratchpad.
