# What We Tested

One line per project — the actual experiment run and what it showed, not just the concept name.

| # | Project Name                      | What We Tested                                                                                                             |
|---|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| 1 | The Worker/Tool-Location Test     | Where AI "thinks" (cloud) vs where tools "act" (device) — tab close, cross-browser, cross-device                           |


| # | Project Name                      | What We Tested                                                                                                             |
|---|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| 2 | The Three-Tier Audit              | Where files actually land — scratch (Tier 1), account (Tier 2), your computer (Tier 3) — and what survives if the account is lost                                                                                                                                                                 |


| # | Project Name                      | What We Tested                                                                                                             |
|---|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| 3 | The Gate Lab                      | Manual vs Auto approval modes — what gets auto-approved, what should escalate, and found Auto mode missed a deletion approval                                                                                                                                                             |


| # | Project Name                      | What We Tested                                                                                                             |
|---|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| 4 | The First Cloud Schedule          | Whether a scheduled workflow can run with the computer off — six design answers (trigger, touch, device-independence, success signal, autonomy, empty case), a public no-auth API script, a GitHub Actions cron schedule — and found only the manual `workflow_dispatch` run was actually proven; true "fired while offline" proof was never captured                                                                                                                  |

| # | Project Name                      | What We Tested                                                                                                             |
|---|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| 5 | Comparative Agent Harness Study | The same low-stakes task tested across Claude Code, a VS Code GitHub Copilot, and plain ChatGPT — observing which could directly reach the filesystem versus which required human action; plus a second Claude Code plan→execute→verify run to examine Loop and Spine — with the correction branch honestly left untested because the first run had nothing wrong to fix.      |


| # | Project Name                      | What We Tested                                                                                                             |
|---|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| 6 | The Portability Drill (Capstone)  | Whether a working workflow (Project 4's Monday Brief) survives if the vendor disappears — reconstructed instructions from tier-3 files only, proven by running it cold in a clean folder — and found the gaps were never in the code, but in a GitHub account-settings toggle and an OS-level Task Scheduler entry that never had a file to land in                                                                                                                 |
