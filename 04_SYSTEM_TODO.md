# BETTERMAN — 04: System TODO (the autonomous layer)
Goal: the system watches, so Mike doesn't have to check in. Runs on HIS hardware (render farm + local models). No dependence on any one AI vendor — frontier models are optional advisors, not infrastructure. Everything reads/writes `data/*.json` in this repo; the dashboard renders whatever lands there.

## Principles
- Read-only by default. The system observes and suggests; Mike acts. Nothing sends, posts, or signs.
- Local models first (Ollama on render nodes). A frontier model may be consulted manually for hard judgment calls.
- Credentials live in a local `.env` on the runner box — NEVER in this repo.
- Every module writes JSON to `data/` + appends to its own log. Git is the transport and the audit trail.

## Modules (build order)

### v0.1 — pulse runner ✅ mostly done
- [x] `scripts/checkpoint.py` with `--ollama` commentary
- [ ] Pick the runner box (one always-on render node)
- [ ] Cron: Sunday 7pm — pull, checkpoint, commit, push
- [ ] Delete/keep the Claude-app scheduled task (redundant once cron works)
- Effort: 1 evening

### v0.2 — scout (opportunity scanner) ← the new capability
- [ ] `scripts/scout.py`: pull RSS/HTML from a source list, local model scores each item against the mission profile, writes top hits to `data/opportunities.json`
- [ ] `data/sources.json` — starter list:
  - News: LAist, LA Times California section, Westside/local patch feeds
  - Government: LA City volunteer opportunities (volunteer.lacity.gov), LA County arts & culture commission, LAUSD/district arts programs, grants.gov RSS (keywords: arts education, youth media, homelessness storytelling), California Volunteers (californiavolunteers.ca.gov), CA Arts Council grant deadlines
  - Sector: Americans for the Arts, photo/documentary fellowship deadlines (CatchLight, etc.)
- [ ] `prompts/scout_filter.md` — the mission profile a local model scores against (problems: homelessness/kids/disconnection; assets: photo, messaging, AI/realtime, events network; constraints: LA, low-cash, burst hours)
- [ ] Dashboard panel: top 3 open opportunities w/ deadlines
- [ ] Cron: 2×/week
- Effort: 1–2 evenings. Highest value per hour of anything on this list.

### v0.3 — mailwatch (email checking, read-only)
- [ ] Decide account: dedicated betterman@ address (cleaner) vs filter on personal Gmail (label "BETTERMAN")
- [ ] `scripts/mailwatch.py`: IMAP read-only (app password in .env), pull labeled/new mail, local model classifies (org reply / league-school thread / opportunity / noise), writes `data/inbox_digest.json`
- [ ] NEVER sends mail. Drafts go to `data/draft_replies/` as text files for Mike to copy.
- [ ] Cron: daily
- Effort: 1–2 evenings

### v0.4 — passive tracker (progress without check-ins)
- [ ] Watch the photo-archive folder: new RAW/exports with EXIF dates → candidate "shoot detected" entries
- [ ] Watch git activity + calendar (ICS feed) for BETTERMAN-tagged events → candidate hours
- [ ] Candidates queue in `data/pending_confirmations.json`; weekly pulse asks Mike yes/no instead of open questions. Confirmation beats self-reporting.
- Effort: 2–3 evenings

### v0.5 — digest (the no-check-in summary)
- [ ] `scripts/digest.py`: assemble checkpoint + scout hits + inbox digest + pending confirmations into one weekly markdown
- [ ] Delivery: SMTP via app password in .env (his own creds, his own send) and/or commit to `digests/` rendered on dashboard
- [ ] Cron: Sunday after pulse
- Effort: 1 evening

### v0.6 — hosting (deferred decision)
- [ ] betterman.mrmichaelmoore.com: Cloudflare Pages (private repo, free, custom domain) vs public mirror repo + GitHub Pages. Decide when dashboard is worth sharing beyond Mike.

## Decisions Mike owes the system
- [ ] Which render node is the always-on runner
- [ ] Dedicated email vs labeled personal Gmail (v0.3)
- [ ] Which local model is the default scorer (llama3? qwen? — pick once, note in sources.json)
- [ ] Hosting path (v0.6)

## What this buys
By v0.5 the system: checks mail, detects progress passively, scans news + government sources for opportunities, grades pace, and hands Mike one weekly digest — all on his own metal, all auditable in git, no vendor in the loop.
