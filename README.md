# BETTERMAN
Mike Moore's 5-year mission (Jun 2026 → Jun 2031): **a storytelling engine for the unseen of Los Angeles.** Measurable impact = minds changed. Started at zero on 2026-06-11.

## If you are an AI reading this (frontier model, local model on the render farm, whoever)
Read in order, then act:
1. `00_INTAKE_21_QUESTIONS.md` — who Mike is, his constraints and values
2. `01_IMPACT_MAP.md` — the 5-year plan, phases, exit criteria, design constraints (non-negotiable)
3. `02_METRICS.md` — what we count and how
4. `data/metrics.json` — **current state. Always read before advising. Always update after progress.**

Update protocol is in 02. Never delete log entries. Respect the design constraints in 01 — they encode values, not preferences.

## If you are Mike
- Open `dashboard/index.html` for the visual state (or serve it: `python3 -m http.server` from repo root → `localhost:8000/dashboard/`)
- Your next actions are the unticked Phase 0 boxes on the dashboard
- Log progress by telling any Claude session "update BETTERMAN metrics: …" or editing `data/metrics.json` yourself

## Structure
```
00_INTAKE_21_QUESTIONS.md   who + why (answered intake)
01_IMPACT_MAP.md            the 5-year map
02_METRICS.md               metric definitions + update protocol
data/metrics.json           LIVE STATE — single source of truth
dashboard/index.html        visual dashboard (static, server-deployable)
```

Private repo. Token-based push access configured on Mike's machine (expires 2026-07-11 — regenerate then).
