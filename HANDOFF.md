# BETTERMAN — HANDOFF
**The complete transfer document.** Written 2026-07-05 (day 25 of 1,826). If you are reading this — human, frontier model, or a local model on Mike's render farm — this file tells you everything needed to operate the project cold. No other session, no other AI's memory, is required.

---

## 1. What this is
Mike Moore (45, Los Angeles, creative director — corporate messaging, events, photography, AI/realtime tech) is running a 5-year mission, June 2026 → June 2031:

**THE BET: A storytelling engine for the unseen of Los Angeles.**
Mike and the young creatives he trains document the people LA looks past — the homeless, the disconnected, kids without a path — through photography, film, and realtime/AI media. Direct service is the act of seeing someone and telling their story right. Impact is measured in **minds changed**. By June 2031 the engine must run without him. Ratified 2026-06-11.

## 2. Read order for a new operator
1. `00_INTAKE_21_QUESTIONS.md` — who Mike is: constraints, values, assets, burnout triggers
2. `01_IMPACT_MAP.md` — the 5-year plan: phases 0–4, exit criteria, design constraints
3. `02_METRICS.md` — the eight numbers, counting rules, update protocol
4. `03_FEEDBACK_LOOP.md` — weekly/checkpoint/quarterly loops, adaptation rules
5. `04_SYSTEM_TODO.md` — the autonomous layer to build on Mike's hardware
6. `data/metrics.json` — **LIVE STATE. Read before advising, update after progress.**

## 3. Non-negotiable design constraints (values, not preferences)
- Family first: never costs son's baseball or Mike's health routine
- Hours: 2/wk floor, 10/wk ceiling — feast-or-famine; plan for bursts, tolerate dead months
- Money: <$1k/yr; every dollar logged (transparency ledger in metrics)
- NO charity-middleman structures. Money and effort go to the work, not institutions
- Mike stays invisible; subjects and mentees are the stars
- Consent/dignity protocol governs every story (not yet drafted — Phase 0 item)
- The plan bends; these constraints don't. Targets move only at quarterly reviews, with reasons logged
- Never delete log entries. Git history is the audit trail

## 4. State as of 2026-07-05
- Phase 0 (Foundation, Jun–Sep 2026). Checklist: intake ✅, repo/tracking ✅, dashboard deploy ☐, org shortlist ☐, consent protocol ☐, Story #001 ☐
- All eight metrics at zero. Checkpoint grade: MIXED (stories/minds/hours behind linear pace; grace period applies elsewhere)
- Two automated pulses ran (Jun 22, Jun 28) — no response from Mike either week; logged as data. One more silent pulse triggers the stall rule: **shrink the next action, don't add ambition**
- Mike's stated direction (2026-07-05): system must run on HIS hardware, not inside any AI vendor's sandbox. Local models first; frontier models are optional advisors

## 5. Infrastructure
- **Repo (source of truth):** github.com/mrmichaelmoorecom-sys/BETTERMAN (private). Local: `/Users/trm/BETTERMAN`. A Dropbox copy exists at `~/Library/CloudStorage/Dropbox/BETTERMAN` (docs mirror — repo wins on conflict)
- **⚠️ ACCESS TOKEN EXPIRES 2026-07-11** (fine-grained PAT "better", Contents r/w, BETTERMAN only; embedded in the repo's git remote URL). Regenerate at github.com/settings/personal-access-tokens and update: `git remote set-url origin https://mrmichaelmoorecom-sys:<NEW_TOKEN>@github.com/mrmichaelmoorecom-sys/BETTERMAN.git`
- **Dashboard:** `dashboard/index.html` — static, self-contained; reads `data/metrics.json` + `data/checkpoint_latest.json`. Serve: `python3 -m http.server` from repo root. Planned home: betterman.mrmichaelmoore.com (hosting undecided — see §7)
- **Checkpoint engine:** `python3 scripts/checkpoint.py` (stdlib only; `--ollama <model>` adds local-AI commentary via localhost:11434). Grades pace, flags stalls >21 days and overspend
- **Prompts (runner-agnostic):** `prompts/weekly_pulse.md`, `prompts/quarterly_review.md` — feed to any agent
- **Claude-app scheduled task** `betterman-weekly-pulse` (Sundays 7pm PT) currently runs the pulse. Mike intends to replace it with cron on a render node:
  `0 19 * * 0 cd ~/BETTERMAN && git pull && python3 scripts/checkpoint.py --ollama llama3 && git add -A && git commit -m "pulse: cron" && git push`
  Once cron is live, delete the Claude task (Scheduled section in app sidebar) to avoid double pulses

## 6. The autonomous layer (to build — full detail in 04_SYSTEM_TODO.md)
v0.1 cron pulse → v0.2 **scout** (scans LAist, LA city/county volunteer + arts programs, grants.gov, CA Arts Council, fellowships; local model scores against mission profile → `data/opportunities.json`) → v0.3 **mailwatch** (read-only IMAP triage; drafts, never sends) → v0.4 **passive tracker** (EXIF/calendar/git signals → confirmation queue) → v0.5 **digest** (one weekly email via Mike's own SMTP). Principles: read-only by default, credentials in local `.env` never in repo, everything lands in `data/*.json`.

## 7. Open decisions (Mike owes these)
1. Hosting for betterman.mrmichaelmoore.com — Cloudflare Pages (private repo, free) vs public mirror + GitHub Pages vs GitHub Pro
2. Which render node is the always-on runner
3. Dedicated email address vs labeled personal Gmail for mailwatch
4. Default local scoring model (llama3? qwen?)
5. Render-farm compute donation (intake said "maybe — depends on use")

## 8. Immediate next actions (in order)
1. **Regenerate the GitHub token before 2026-07-11** — everything downstream needs push access
2. Stand up cron pulse on a render node; delete the Claude-app task
3. Draft the consent/dignity protocol (most important unwritten document — blocks Story #001)
4. Shortlist 5 LA orgs to embed with (homelessness/youth/connection; vet for low overhead)
5. Shoot Story #001 — one person, seen properly. This unblocks everything psychological
6. Build scout (v0.2) — the "what am I missing" scanner Mike asked for

## 9. Operating notes for AI operators
- Mike is visual: lead with the dashboard, status bars, checklists — not walls of text
- He distrusts overhead and vendor lock-in; never propose structures that skim or platforms that trap
- Feast-or-famine schedule: when he goes quiet, shrink asks to 2-minute actions; never guilt him — silence is data, not failure
- He self-describes "no longer a coder": give him copy-paste commands, not exercises
- Update protocol: bump `data/metrics.json`, append log entry, re-run checkpoint, commit with a reason, push
- The 2031 test of every decision: does this make the engine more able to run without Mike, and without you?

*End of handoff. The mission continues with whoever reads this.*
