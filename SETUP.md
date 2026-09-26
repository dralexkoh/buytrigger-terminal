# SETUP — getting this package into the `buytrigger-swarm` repo

Five minutes on the Mac. Nothing here touches the dashboard repo.

## 1. Create the empty repo on GitHub

GitHub → New repository → name `buytrigger-swarm` → Private → **do not** add a README, .gitignore or licence (this package has them) → Create.

## 2. Clone it next to the other projects

Terminal:

```bash
cd "$HOME/Desktop/GitHub Project"
git clone https://github.com/dralexkoh/buytrigger-swarm.git
```

(If the repo is under a different GitHub user or org, use that URL. The folder name should be `buytrigger-swarm`.)

## 3. Drop the package in

The archive is in two places: the chat (`buytrigger-swarm-package-2026-09-26.tar.gz`) and the dashboard folder under `Claude outputs/` (same file; it is untracked there, do not commit it to the dashboard repo). It unpacks to a folder called `buytrigger-swarm-package/`. Copy that folder's contents into the clone, so that `README.md`, `bees/`, `tools/` and the rest sit at the top level of `buytrigger-swarm`.

```bash
cd "$HOME/Desktop/GitHub Project"
tar -xzf "buytrigger-dashboard/Claude outputs/buytrigger-swarm-package-2026-09-26.tar.gz"
cp -R buytrigger-swarm-package/. buytrigger-swarm/
rm -r buytrigger-swarm-package
```

(A `.zip` with the same contents is in the chat too, if double-clicking is easier.)

## 4. First commit

```bash
cd "$HOME/Desktop/GitHub Project/buytrigger-swarm"
git add -A
git commit -m "swarm: bees, rules, tools, schema, ledger snapshots (26 Sep 2026)"
git push -u origin main
```

## 5. Connect the folder in the Claude desktop app

In the Cowork task for the swarm: **Add folder** → choose `Desktop/GitHub Project/buytrigger-swarm`. From then on the swarm chat works in that folder directly: prompt changes, ledger snapshots, tool updates, dated close-outs.

## Then, when you have a minute

- **Allow the upload host** so the Layer 2 bee can attach its charts to the Typefully draft instead of leaving them as files: add `typefully-user-uploads.s3.amazonaws.com` to the allowed domains for Claude. Until then, marketing attaches the PNGs by hand (the draft's scratchpad says which chart goes on which post).
- **Check the Layer 1 schedule.** The task is named "4x weekdays" but its schedule is 07:25 and 16:25 UK (two runs). If two is what you want, fine; if you want four, `bees/SCHEDULE.md` has the line to change.
- **Bios.** Put the tagged links in the X and Threads bios (`rules/platforms.md`, "Tracked links"). X posts cannot carry a link, so X attribution comes from the bio.

## Naming convention (so chats never clash again)

One job = one chat = one branch, named `<job>-<stage>`. The swarm's branches live in this repo; the dashboard's in the dashboard repo; the CRM's in whichever repo the CRM chat owns. `docs/naming-convention.md` has the full note.
