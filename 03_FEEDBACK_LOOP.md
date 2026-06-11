# BETTERMAN — 03: The feedback loop
A plan that can't hear itself fail is a wish. This is how BETTERMAN adapts.

## Three loops, three speeds

### 1. Weekly pulse (automated, ~2 min of Mike's time)
A Claude scheduled task runs weekly: reads `data/metrics.json`, runs `scripts/checkpoint.py`, and asks Mike up to 3 questions ("any stories this week? hours? anything blocking?"). Answers get written to metrics + log, committed, pushed. If nothing happened, that gets logged too — silence is data.

### 2. Checkpoint engine (scripted, runs anywhere)
`python3 scripts/checkpoint.py` — stdlib only; runs on the M4, render farm, or any server/cron.
- Compares every metric to linear pace → ahead / on_pace / behind
- Flags stalls (no log entry in 21 days)
- Flags overspend vs the $1k/yr cap
- Emits `data/checkpoint_latest.json` → the dashboard renders it as the "last checkpoint" panel
- Optional `--ollama [model]` flag: a local model on the render farm adds blunt 3-sentence commentary. Free compute, no cloud dependency.

### 3. Quarterly review (human + AI, ~1 hr)
Sit down with any Claude session: "run the BETTERMAN quarterly." It reads 00–03 + metrics + checkpoints and challenges the plan itself, not just the pace:
- Are exit criteria for the current phase still right?
- Is any metric measuring the wrong thing? (e.g. minds_reached counting method)
- What did the log say that the plan didn't predict?
- Output: a `QUARTERLY_YYYY_QN.md` review file + amendments to 01/02 as needed, committed.

## Adaptation rules
- The plan bends, the constraints don't. Design constraints in 01 (family, budget cap, no-overhead rule, invisibility) survive every revision.
- Every plan change is a commit with a reason in the message. Git history = the project's evolution record.
- Two consecutive "stalled" checkpoints → the next session's first job is shrinking the next action until it fits inside a bad week, not adding ambition.
- Targets can move — but only at quarterly reviews, never in the weekly pulse, and the log entry must say why.

## Failure modes this catches
| Signal | Catch |
|---|---|
| Busy season swallows the project | Stall flag at 21 days; weekly pulse keeps a 2-min toehold |
| Vanity progress (hours logged, no stories) | Per-metric pace verdicts diverge — visible on dashboard |
| Plan drift from values | Quarterly review re-reads intake (00) every time |
| Overspend creep | Budget pace check every checkpoint |
| AI dependence | Checkpoint is plain Python; repo is plain markdown; any model or human can drive |
