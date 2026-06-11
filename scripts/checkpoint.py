#!/usr/bin/env python3
"""BETTERMAN checkpoint — the feedback loop.
Reads data/metrics.json, judges pace vs plan, writes data/checkpoint_latest.json
(which the dashboard displays) and prints a human report.

Run from repo root:  python3 scripts/checkpoint.py
Optional local-AI commentary (render farm / Ollama):
                     python3 scripts/checkpoint.py --ollama [model]
No dependencies beyond stdlib. Safe to run from cron, a render node, or by hand.
"""
import json, sys, datetime, pathlib, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "metrics.json"
OUT  = ROOT / "data" / "checkpoint_latest.json"

STALL_DAYS = 21          # no log entry for this long => stalled flag
BEHIND = 0.6             # progress/expected below this => behind
AHEAD  = 1.25            # above this => ahead

def main():
    d = json.loads(DATA.read_text())
    today = datetime.date.today()
    start = datetime.date.fromisoformat(d["started"])
    end   = datetime.date.fromisoformat(d["horizon"])
    frac  = max(0.001, min(1.0, (today - start).days / (end - start).days))

    verdicts, flags = {}, []
    for key, m in d["metrics"].items():
        if "dollar" in key:
            # budget: flag only if burn rate exceeds cap pace
            expected = m["target_2031"] * frac
            verdicts[key] = "ok" if m["value"] <= expected else "overspend"
            if verdicts[key] == "overspend":
                flags.append(f"Spending ahead of cap: ${m['value']} vs ${expected:.0f} pace")
            continue
        expected = m["target_2031"] * frac
        ratio = (m["value"] / expected) if expected else 0
        verdicts[key] = "ahead" if ratio >= AHEAD else "behind" if ratio < BEHIND else "on_pace"
        if verdicts[key] == "behind":
            flags.append(f"{m['label']}: {m['value']} vs {expected:.1f} expected")

    last_log = max(e["date"] for e in d["log"])
    stale_days = (today - datetime.date.fromisoformat(last_log)).days
    if stale_days > STALL_DAYS:
        flags.append(f"STALLED: no log entry in {stale_days} days. Smallest possible next action?")

    unchecked = [c["item"] for c in d.get("checklist_phase0", []) if not c["done"]]
    behind_ct = sum(1 for v in verdicts.values() if v == "behind")
    grade = ("stalled" if stale_days > STALL_DAYS else
             "behind" if behind_ct >= 4 else
             "mixed"  if behind_ct >= 1 else "on_track")

    report = {
        "checkpoint_date": today.isoformat(),
        "day": (today - start).days + 1,
        "elapsed_pct": round(frac * 100, 1),
        "grade": grade,
        "verdicts": verdicts,
        "flags": flags,
        "next_actions": unchecked[:3],
        "days_since_last_log": stale_days,
        "ai_commentary": None,
    }

    if "--ollama" in sys.argv:
        model = sys.argv[sys.argv.index("--ollama") + 1] if len(sys.argv) > sys.argv.index("--ollama") + 1 else "llama3"
        try:
            prompt = ("You are the feedback loop for a 5-year personal impact project. "
                      "Given this checkpoint JSON, give 3 blunt sentences: what's working, "
                      "what's slipping, the single next action. JSON: " + json.dumps(report))
            req = urllib.request.Request("http://localhost:11434/api/generate",
                json.dumps({"model": model, "prompt": prompt, "stream": False}).encode(),
                {"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                report["ai_commentary"] = json.loads(r.read())["response"].strip()
        except Exception as e:
            report["ai_commentary"] = f"(ollama unavailable: {e})"

    OUT.write_text(json.dumps(report, indent=2))
    print(f"BETTERMAN checkpoint — day {report['day']}, {report['elapsed_pct']}% elapsed — grade: {grade.upper()}")
    for f in flags: print("  ⚑", f)
    for a in report["next_actions"]: print("  →", a)
    if report["ai_commentary"]: print("\nAI:", report["ai_commentary"])
    print(f"\nwrote {OUT.relative_to(ROOT)} — commit it so the dashboard and future sessions see it.")

if __name__ == "__main__":
    main()
