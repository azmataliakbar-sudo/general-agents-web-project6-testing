#!/usr/bin/env python3
"""
Monday Brief Generator
Project 4: The First Cloud Schedule

Generates a Monday morning brief from cloud-reachable public sources:
- GitHub trending repos
- Hacker News top stories

Writes output to output/monday-brief-YYYY-MM-DD.md (tier 3).
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

# Cloud-reachable, no-auth public APIs
GITHUB_API = "https://api.github.com/search/repositories?q=created:>YYYY-MM-DD&sort=stars&order=desc&per_page=10"
HN_API = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM_API = "https://hacker-news.firebaseio.com/v0/item/{id}.json"


def safe_get(url, timeout=15):
    """GET with error capture. Returns (status, json_or_text, error_str)."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "monday-brief/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read().decode("utf-8", errors="replace")
            return resp.status, data, None
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode("utf-8", errors="replace")
        except Exception:
            body = ""
        return e.code, body, f"HTTPError: {e.reason}"
    except urllib.error.URLError as e:
        return 0, "", f"URLError: {e.reason}"
    except Exception as e:
        return 0, "", f"Error: {type(e).__name__}: {e}"


def fetch_github_trending():
    """Fetch repos created in the last 7 days, sorted by stars."""
    today = datetime.now(timezone.utc)
    from datetime import timedelta
    week_ago = (today - timedelta(days=7)).strftime("%Y-%m-%d")
    url = GITHUB_API.replace("YYYY-MM-DD", week_ago)
    status, data, err = safe_get(url)
    if err or status != 200:
        return {"ok": False, "error": err or f"status {status}", "items": []}
    try:
        payload = json.loads(data)
        items = []
        for r in payload.get("items", [])[:10]:
            items.append({
                "name": r.get("full_name", ""),
                "description": (r.get("description") or "").strip(),
                "stars": r.get("stargazers_count", 0),
                "url": r.get("html_url", ""),
                "language": r.get("language") or "—",
            })
        return {"ok": True, "items": items, "count": payload.get("total_count", 0)}
    except json.JSONDecodeError as e:
        return {"ok": False, "error": f"JSON decode: {e}", "items": []}


def fetch_hn_top(limit=10):
    """Fetch top HN story titles."""
    status, data, err = safe_get(HN_API)
    if err or status != 200:
        return {"ok": False, "error": err or f"status {status}", "items": []}
    try:
        ids = json.loads(data)[:limit]
        items = []
        for sid in ids:
            s_status, s_data, s_err = safe_get(HN_ITEM_API.format(id=sid))
            if s_err or s_status != 200:
                continue
            try:
                s = json.loads(s_data)
                if s and s.get("title"):
                    items.append({
                        "title": s.get("title", ""),
                        "score": s.get("score", 0),
                        "comments": s.get("descendants", 0),
                        "url": s.get("url") or f"https://news.ycombinator.com/item?id={sid}",
                        "hn": f"https://news.ycombinator.com/item?id={sid}",
                    })
            except json.JSONDecodeError:
                continue
        return {"ok": True, "items": items}
    except json.JSONDecodeError as e:
        return {"ok": False, "error": f"JSON decode: {e}", "items": []}


def render_brief(github, hn, run_ts, out_path):
    """Render the Markdown brief and write to disk."""
    lines = []
    lines.append(f"# Monday Brief — {run_ts.strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append(f"_Generated: {run_ts.isoformat()}_")
    lines.append("")
    lines.append("---")
    lines.append("")

    # GitHub section
    lines.append("## Trending on GitHub (last 7 days)")
    lines.append("")
    if github["ok"] and github["items"]:
        lines.append(f"_{github['count']} new repos; top 10 shown_")
        lines.append("")
        for i, r in enumerate(github["items"], 1):
            desc = r["description"] or "_no description_"
            lines.append(f"{i}. **[{r['name']}]({r['url']})** ⭐ {r['stars']} · `{r['language']}`")
            lines.append(f"   {desc}")
            lines.append("")
    else:
        lines.append("> No data available.")
        if github.get("error"):
            lines.append(f"> Error: `{github['error']}`")
        lines.append("")

    lines.append("---")
    lines.append("")

    # HN section
    lines.append("## Top Stories on Hacker News")
    lines.append("")
    if hn["ok"] and hn["items"]:
        for i, s in enumerate(hn["items"], 1):
            lines.append(f"{i}. **[{s['title']}]({s['url']})**")
            lines.append(f"   ↑ {s['score']} · 💬 {s['comments']} · [HN]({s['hn']})")
            lines.append("")
    else:
        lines.append("> No data available.")
        if hn.get("error"):
            lines.append(f"> Error: `{hn['error']}`")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Run Metadata")
    lines.append("")
    lines.append(f"- Trigger: scheduled")
    lines.append(f"- Sources: GitHub API, Hacker News API (public, no auth)")
    lines.append(f"- Tier: 3 (file on disk)")
    lines.append(f"- Autonomy: read-only, no sends, no deletions")
    lines.append("")

    out = "\n".join(lines)
    out_path.write_text(out, encoding="utf-8")
    return out


def main():
    here = Path(__file__).parent
    out_dir = here / "output"
    out_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc)
    out_file = out_dir / f"monday-brief-{now.strftime('%Y-%m-%d')}.md"

    github = fetch_github_trending()
    hn = fetch_hn_top(10)
    body = render_brief(github, hn, now, out_file)

    # Success signal: file exists and is non-empty
    if out_file.exists() and out_file.stat().st_size > 0:
        print(f"OK: wrote {out_file} ({out_file.stat().st_size} bytes)")
        print(f"     github.ok={github['ok']} hn.ok={hn['ok']}")
        return 0
    else:
        print(f"FAIL: brief not written", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
