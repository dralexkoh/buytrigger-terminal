# Rename to the Terminal — the steps (29 Sep 2026)

Done by Claude already:
- All six scheduled tasks renamed `3.7.15 Terminal · …` (writer, watchdog, L1, L2, L3, Lisa desk). Schedules, prompts and models untouched.
- Project docs updated: `claude/START-HERE.md`, `claude/terminal-blueprint.md`, `claude/control-room-brief.md`.
- Repo docs updated for the new name (README, SETUP, SCHEDULE, LOG) and committed on the Mac.

Alex's steps, in order (about 5 minutes):

## 1. Rename the Claude project
Project settings → name → **BuyTrigger Newsroom Terminal (BTRES-3.7.15)** → save.
Then in the same settings, Instructions: replace the whole text with the block at the bottom of this file.

## 2. Rename the GitHub repo
github.com/dralexkoh/buytrigger-swarm → Settings → Repository name → **buytrigger-terminal** → Rename.
(GitHub keeps the old name as a redirect, so nothing breaks.)

## 3. Rename the folder on the Mac and point it at the new address
Terminal (the Mac app), paste all four lines:
```bash
cd "$HOME/Desktop/GitHub Project"
mv buytrigger-swarm buytrigger-terminal
cd buytrigger-terminal
git remote set-url origin https://github.com/dralexkoh/buytrigger-terminal.git
```

## 4. Reconnect the folder in the Claude project
Project → folders: remove `buytrigger-swarm`, add `Desktop/GitHub Project/buytrigger-terminal`.

## 5. Push (needs the GitHub token to include the new repo — see START-HERE open items)
```bash
cd "$HOME/Desktop/GitHub Project/buytrigger-terminal"
git push -u origin main
```

## 6. Tell the chat "renamed"
Claude then checks the folder, the remote and the push, and updates the LOG.

---

## Project instructions to paste (step 1)

BuyTrigger Newsroom Terminal — work item BTRES-3.7.15. One machine: gather market news once (Tim's research desk), publish it to buytrigger.club and the members' Desk, broadcast it as L1 headlines, L2 threads with graphics, L3 articles, L4 video (later) and Telegram, measure what worked, control it from one screen.
Every chat and task carries one label: 3.7.15 Terminal · Newsroom, · Broadcast, · Control Room, or · Desk feed.
Before doing anything, read claude/START-HERE.md and claude/terminal-blueprint.md, then docs/START-HERE.md in the buytrigger-terminal folder.
Rules: everything reads the feed and nothing downstream researches; Colette then Lisa review before anything auto-publishes; at most 5 posts a day on the account, 45 minutes apart; no change to a live task without two test runs of a copy that publishes nothing; never print or move the filing-token line; nothing about Alex's positions, trades, holdings, subscribers or revenue; AI video is labelled as AI.
Alex decides models, schedules, what publishes, new channels and anything member-facing. Plain language, one decision at a time, outcome first. The members' app stays in the BuyTrigger Dashboard project.
