# Lock-In Exposure: What Could NOT Be Reconstructed

This is the required deliverable for Project 6: a written list of what
survives tier-3-only reconstruction of the Monday Brief workflow (Project 4),
and what does not. Anything on the "could not reconstruct" side is exposure
to whichever vendor holds it — that's the portability backlog.

## Reconstructed successfully (survives)

- The full script logic, fetch/render/write behavior — `monday_brief.py` is
  self-contained, uses only the Python standard library, and has no hardcoded
  absolute paths (`Path(__file__).parent`), so it ran unmodified from a brand
  new folder.
- The design rationale (trigger, touch, device-independence, success signal,
  autonomy, empty-case) — all captured in `README.md` / `WALKTHROUGH.md` as
  plain text, not vendor session memory.
- The cloud-schedule definition — the cron expression, the runner steps, and
  the commit-back step are all in `.github/workflows/monday-brief.yml`,
  which is a committed file, not a vendor UI setting.
- The "done" checklist and the exact pass/fail condition — documented in
  `WALKTHROUGH.md`, not inferred from memory.
- A working deliverable — re-ran today (2026-09-08) from a clean copy and
  produced a fresh, live-data brief in ~1 second, with no credentials.

## Could NOT be reconstructed from tier-3 files alone

1. **GitHub repo Actions permission toggle.**
   `Settings → Actions → General → Workflow permissions → "Read and write"`
   is a setting stored in GitHub's own account database, not in any file in
   the repo. A fresh clone/fork of this exact repo would silently fail to
   push its results until a human re-clicks that toggle. The *fact* that
   this step exists was rescued because it was written into `README.md` —
   if it hadn't been written down, this would be a total loss, since it
   leaves no trace in git history at all.

2. **The original GitHub account/auth mismatch and its fix.**
   `README.md` records *that* a wrong cached GitHub login caused a 403, and
   *that* switching accounts fixed it — but not the exact commands, error
   text, or git-credential-manager state involved. The troubleshooting
   process itself lived only in the original chat session and is gone.

3. **The registered local Windows Scheduled Task.**
   `WALKTHROUGH.md` documents the PowerShell needed to *create* a
   `MondayBrief` Task Scheduler entry, but the actual registered task object
   (if it was ever run) lives in this Windows machine's Task Scheduler
   store, not in any tier-3 file. Reinstalling Windows loses it even though
   the recipe to recreate it survives.

4. **Proof that the cloud schedule fired unattended, computer off.**
   The WALKTHROUGH "Done When" list still has this unchecked. The one proof
   artifact that exists (`test/output/test-brief-2026-09-07-104810.md`) shows
   a *manual* `workflow_dispatch` test run, not an actual `cron`-triggered
   run with the local machine powered off. That specific evidence does not
   exist yet in any tier, reconstructable or not — it's a gap in the
   original work, not just a portability gap.

5. **Why 09:00 UTC / Monday specifically.**
   The chosen cron time is recorded as a fact (`0 9 * * 1`), but the
   reasoning behind that specific choice (timezone convenience, "start of
   week" framing, anything else discussed) was session conversation, not
   committed anywhere.

6. **The AI vendor's standing instructions/memory that produced this
   discipline in the first place.**
   The habit of "every deliverable states its tier" and "success signal
   must be a tier-3 file" is enforced in this session by an `Instructions`
   layer (this repo's `CLAUDE.md` conventions) that is itself vendor-hosted
   configuration for the *current* coding assistant. If that vendor
   disappeared, the discipline would need to be re-derived from reading
   `project_2/README.md` and this file — it is not separately backed up as
   its own portable policy document.

## The backlog this creates

- Write down the exact GitHub Actions permission click-path as a **repo
  setup script or repo-level `CODEOWNERS`/settings-as-code file** (GitHub
  supports some settings via `.github/settings.yml` with a third-party
  Probot app) so it isn't tribal knowledge.
- Capture troubleshooting steps (auth fixes, error text) in a `docs/incidents.md`
  at the time they happen, not just the one-line summary that made it into
  `README.md` this time.
- Either get the real "fired while computer was off" proof, or update the
  done-criteria to reflect what was actually verified (`workflow_dispatch`
  only) so future-you isn't misled by an unchecked box.
- Export the local Task Scheduler registration command into the repo (it
  already is, in `WALKTHROUGH.md` — the backlog item is: actually test that
  recipe on a second machine to confirm it's complete).
- Consider Concept 11's open path: this workflow's only remaining vendor
  dependency for "runs with the computer off" is GitHub Actions itself. A
  fully vendor-cloud-free version would replace the Actions runner with a
  self-hosted cron box (OpenCode-style) — full custody, but the team then
  owns uptime, retries, and secrets management that GitHub currently
  provides for free.
