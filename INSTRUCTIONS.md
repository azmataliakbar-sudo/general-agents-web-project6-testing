# Reconstructed Workflow: The Monday Brief

> **Reconstruction rule for this document**: every line below was derived
> ONLY from tier-3 files that survive on disk / in the git repo — no memory
> of the original build session, no vendor chat history, no vendor account
> state was consulted. Sources are cited inline as `[source: file]`.

## What this workflow does

Fetches two public, auth-free feeds — GitHub repos created in the last 7
days (sorted by stars) and the current Hacker News top stories — and
renders them into one dated Markdown brief.
`[source: project_4/monday_brief.py, docstring + fetch_github_trending() + fetch_hn_top()]`

## Source locations (where everything lives)

| Artifact | Path | Tier |
|---|---|---|
| Generator script | `project_4/monday_brief.py` | 3 (committed to git) |
| Design record (six answers) | `project_4/README.md` | 3 |
| Run log / setup notes | `project_4/WALKTHROUGH.md` | 3 |
| Cloud schedule definition | `project_4/.github/workflows/monday-brief.yml` | 3 |
| Fast-test variant | `project_4/test/monday_brief2.py` + `.github/workflows/test-schedule.yml` | 3 |
| Output deliverables | `project_4/output/monday-brief-*.md` | 3 |
| Remote system of record | `github.com/azmataliakbar-sudo/general-agents-web-project4-testing` | 3 (user-owned repo) |

`[source: README.md "Actual Results"; WALKTHROUGH.md "Cloud-Reachable Sources"; git ls-files]`

## How to run it (manual)

```bash
cd project_4
python monday_brief.py
```

Expected: `output/monday-brief-YYYY-MM-DD.md` is created, non-empty, containing
a "Trending on GitHub" section and a "Top Stories on Hacker News" section.
`[source: monday_brief.py main(); WALKTHROUGH.md "Walk #1 / Walk #2"]`

No API keys, tokens, or logins are required — both endpoints are public:
- `https://api.github.com/search/repositories?q=created:>YYYY-MM-DD&sort=stars`
- `https://hacker-news.firebaseio.com/v0/topstories.json`
`[source: monday_brief.py GITHUB_API / HN_API constants]`

## How to run it unattended (cloud schedule)

The repo already contains a GitHub Actions workflow that:
1. Fires on cron `0 9 * * 1` (every Monday 09:00 UTC) or on manual `workflow_dispatch`
2. Checks out the repo, installs Python 3.12
3. Runs `python monday_brief.py`
4. Commits the new file in `output/` back to the repo

`[source: .github/workflows/monday-brief.yml, verbatim steps]`

To reactivate it on a fresh copy of this repo, the workflow file needs no
edits — pushing the repo to GitHub with Actions enabled is sufficient,
**except** for one non-file setting described in `lock-in-exposure.md`
(repo → Actions → Workflow permissions must allow "Read and write").
`[source: README.md "Missing write permissions" note]`

## Definition of done

Reconstructed directly from `WALKTHROUGH.md`'s own checklist:

- [x] Two manual runs each produce a dated brief file in `output/`
- [ ] Cloud schedule has fired at least twice with the local computer off
- [ ] Each fired run leaves a verifiable tier-3 success signal (the dated file)

Success signal, precisely as coded: the script exits 0 only if the output
file exists on disk and its size is greater than 0 bytes.
`[source: monday_brief.py main(), the `if out_file.exists() and out_file.stat().st_size > 0` check]`

## Last deliverable

The most recent artifact found on disk at reconstruction time:

- `project_4/output/monday-brief-2026-09-07.md` (manual run)
- `project_4/test/output/test-brief-2026-09-07-104810.md` (cloud-fired proof run,
  confirmed by `git pull` per README.md)

Both are plain Markdown files, readable without any vendor tool.
