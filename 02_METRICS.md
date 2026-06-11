# BETTERMAN — 02: Metrics
Source of truth: `data/metrics.json`. The dashboard reads it; humans and AIs update it. Every update gets a `log` entry — the log is the project's memory.

## The eight numbers
| Metric | 2031 target | Why it matters |
|---|---|---|
| Stories told | 150 | The atomic unit of the work. One person, seen properly. |
| Minds reached | 500,000 | Mike's chosen impact definition. Log the counting method per entry — no inflated reach. |
| Mentees trained | 25 | The engine's cylinders. |
| Engine coefficient | 5 | Mentees who now teach others. THE 2031 metric — proves it runs without Mike. |
| Service hours | 1,000 | Honest accounting of time given. ~4 hr/wk average over 5 years. |
| Orgs embedded | 3 | Phase 1 depth — trusted inside, not visiting. |
| Public showings | 10 | Where the event-production network gets activated. |
| Dollars spent | ≤$5k total | Transparency ledger. Every dollar logged. The anti-overhead rule made visible. |

## Update protocol (human or AI)
1. Edit `data/metrics.json`: bump values, set `updated`, append a `log` entry (date + what happened).
2. Tick `checklist_phase0` items as they complete; when a phase ends, replace with next phase's checklist from 01_IMPACT_MAP.md.
3. Commit with message `metrics: <what changed>`. Push.
4. Never delete log entries. Corrections get new entries.

## Counting rules
- A "story told" = published/exhibited with subject consent per protocol. Drafts don't count.
- "Minds reached" = documented views, verified attendance, or org-reported audience. Estimate conservatively; note method.
- A "mentee trained" = completed a cohort or ≥10 hrs of 1-on-1, produced at least one story.
- Engine coefficient only counts mentees who taught a session without Mike present.
