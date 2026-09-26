# Naming convention — one job, one chat, one branch

Agreed 25 Sep 2026 after two chats built the same CRM package on the same day.

- **One job = one chat = one branch.** A chat owns exactly one job. It works on one branch named `<job>-<stage>`, in the repo that job belongs to (`rules/ownership.md`).
- **Branch names:** `swarm-l2-crosslayer`, `newsroom-web-join`, `crm-stage1`, `dashboard-3.18-desk`. Lower case, hyphens, the job first.
- **Say it in the first message.** The chat states its job, its repo and its branch before it builds anything.
- **Read before building.** `Project/INDEX.md`, the docs in `Project/active/` (or the Project's `claude/` docs), and a search of the Project for the job name. If a handover already exists, that chat owns the job and the new chat stops.
- **Handover, not overlap.** When a job needs something another chat owns (the swarm needs a tracked-link registry the CRM chat owns), it asks through Alex or the Project doc; it does not rebuild it.
- **Close out with a date.** Every job ends with a dated close-out in the Project (`claude/<job>.md`) and in the repo's `docs/LOG.md`: what changed, what was tested, what is left, and Alex's actions.
- **Prompts are files.** A scheduled task's prompt lives in the repo (`bees/`) and is pasted into the task; the file is the source of truth, git is the version history.
