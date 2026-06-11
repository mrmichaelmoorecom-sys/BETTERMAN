# Prompt: weekly pulse
Runner-agnostic. Feed this to any agent (Claude scheduled task, Claude Code, local model on the render farm, or a human with 10 minutes). The Claude desktop scheduled task `betterman-weekly-pulse` (Sundays 7pm PT) uses this same prompt.

---

You are running the weekly pulse for BETTERMAN, Mike's 5-year impact project (a storytelling engine for the unseen of Los Angeles, Jun 2026 → Jun 2031).

Repo: github.com/mrmichaelmoorecom-sys/BETTERMAN (private). Local working copy: /Users/trm/BETTERMAN. Read README.md first if unsure of structure.

Steps:
1. `git pull`, then read data/metrics.json and data/checkpoint_latest.json.
2. Run `python3 scripts/checkpoint.py` from the repo root (add `--ollama <model>` if a local model is available).
3. Ask Mike up to 3 short questions: (a) any stories/shoots/service this week? (b) roughly how many hours did BETTERMAN get? (c) anything blocking, or any spend? Keep it to 2 minutes of his time. If he doesn't respond, log "no response this week" — silence is data.
4. Update data/metrics.json: bump values per his answers, set "updated" to today, append a log entry (date + one-line summary). Tick completed checklist items.
5. Re-run scripts/checkpoint.py so checkpoint_latest.json reflects the update.
6. Commit: "pulse: <date> — <one-line summary>". Push.
7. End with a 3-sentence summary: pace verdict, one thing going well, the single most important next action.

Constraints (never violate): never delete log entries; the plan bends but the design constraints in 01_IMPACT_MAP.md don't; if two consecutive checkpoints are stalled, shrink the next action instead of adding ambition. If anything breaks, say exactly what broke — don't work around it silently.
