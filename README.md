# Project 6: The Portability Drill (Capstone)

**Difficulty**: Capstone | **Time**: 60 min | **Uses**: Concepts 4, 5, 10, and 11

---

## The Drill

> Pretend your preferred vendor disappears tomorrow. Using only tier-3 files
> and user-owned context, reconstruct one working workflow: instructions,
> source locations, definition of done, and last deliverable. Done when you
> have a written list of what you could not reconstruct. That list is your
> lock-in exposure and your next portability backlog.

## What Are Concepts 4, 5, 10, and 11?

| Concept | Name | What It Teaches |
|---------|------|-----------------|
| **Concept 4** | The Account Spine (State Layers) | Persistence has layers: Session / Project / Memory / Instructions / Files — only the last one is yours by default |
| **Concept 5** | The Three File Tiers | Tier 1 (scratch) and tier 2 (platform account) die with the vendor; only tier 3 (your custody) survives |
| **Concept 10** | Pick the Surface by What the Work Touches | Route by data location, runtime, and custody needs — not by product preference |
| **Concept 11** | The Open Path: No Vendor Cloud | Self-hosted alternatives (OpenWork/OpenCode-style) trade a free managed spine for full custody + operator overhead |

## Workflow Chosen

**Project 4's "Monday Brief"** — a scheduled agent workflow that fetches
public GitHub-trending and Hacker-News data and writes a dated Markdown
brief. It was picked because it already lives entirely in tier 3: one
Python script, two README/walkthrough files, and a GitHub Actions workflow
file, all committed to a user-owned git repo.

## Method

1. **No memory allowed.** The reconstruction in `INSTRUCTIONS.md` was
   written by reading only `project_4/monday_brief.py`, `README.md`,
   `WALKTHROUGH.md`, and `.github/workflows/monday-brief.yml` — not by
   recalling how the original session built it.
2. **Prove it, don't just claim it.** The script was copied into a clean
   folder (`reconstruction-test/`) with none of project_4's other state,
   and run following only the reconstructed instructions.
3. **Result**: it worked on the first try — wrote a fresh, live-data brief
   (`reconstruction-test/output/monday-brief-2026-09-08.md`, 4511 bytes,
   `github.ok=True hn.ok=True`) with zero credentials and zero vendor
   session context.
4. **Audit what's missing.** Everything that could *not* be pulled from a
   tier-3 file — a GitHub account-settings toggle, an OS-level scheduled
   task, unwritten troubleshooting steps, the reasoning behind a config
   choice — is listed in `lock-in-exposure.md`.

## Files for Project 6

```
project_6/
├── README.md                          ← this file
├── INSTRUCTIONS.md                    ← the portable, tier-3-only reconstruction (the deliverable)
├── lock-in-exposure.md                ← the required "what could not be reconstructed" list
└── reconstruction-test/
    ├── monday_brief.py                ← clean-room copy, no shared state with project_4
    └── output/
        └── monday-brief-2026-09-08.md ← proof the reconstruction actually runs
```

## Done Criteria (met)

- [x] Instructions readable and executable by someone unfamiliar with the original session — `INSTRUCTIONS.md`, verified by running it cold
- [x] Deliverable lands in tier 3 — `reconstruction-test/output/monday-brief-2026-09-08.md`, a plain file on disk
- [x] Evidence that outputs survive removal from platform custody — the script has no hardcoded paths, no API keys, and no dependency on the original project_4 folder or any chat session
- [x] Written list of what could not be reconstructed — `lock-in-exposure.md`

## Key Insight

Good tier-3 discipline in Project 4 (writing the *design*, not just the
*code*, into `README.md`/`WALKTHROUGH.md`) is what made this reconstruction
possible at all. The gaps that remain aren't in the script — they're in
account-level settings (GitHub's permissions toggle) and OS-level state
(Windows Task Scheduler) that never had a file to land in. **The portability
backlog is exactly the set of things that only ever lived as a click, not a
commit.**
