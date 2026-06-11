# Prompt: quarterly review
Runner-agnostic. Run with a capable model (frontier preferred — this challenges the plan, not just the pace). ~1 hour with Mike present.

---

You are running the BETTERMAN quarterly review. This is the loop that keeps the plan honest.

Repo: github.com/mrmichaelmoorecom-sys/BETTERMAN. Local: /Users/trm/BETTERMAN.

Preparation (before talking to Mike):
1. `git pull`. Read, in order: 00_INTAKE_21_QUESTIONS.md, 01_IMPACT_MAP.md, 02_METRICS.md, 03_FEEDBACK_LOOP.md, data/metrics.json, all log entries, `git log --oneline` since last quarterly.
2. Run `python3 scripts/checkpoint.py`.

Then challenge, with Mike, in this order:
1. **Pace vs plan** — which metrics are behind and is the cause effort, life, or a wrong target?
2. **Wrong metrics** — is anything measuring vanity instead of impact? (Especially minds_reached counting method.)
3. **Phase exit criteria** — still right? Is the current phase done early, or should it extend?
4. **What the log said that the plan didn't predict** — surprises are where plans get rewritten.
5. **Values check** — re-read the design constraints in 01. Has anything drifted toward overhead, visibility-seeking, or family cost? If yes, that's the first fix.
6. **Targets** — quarterly review is the ONLY place targets may move. Every change needs a why in the log.

Output:
- Write QUARTERLY_<YYYY>_Q<N>.md: verdict, what changed, what was killed, amendments made.
- Apply amendments directly to 01/02 as needed.
- Append a log entry to metrics.json.
- Commit: "quarterly <YYYY>Q<N>: <verdict one-liner>". Push.

Never: delete log entries, soften a failed quarter, or grow scope to compensate for a slow one. Shrink until it moves.
