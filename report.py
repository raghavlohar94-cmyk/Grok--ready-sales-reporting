"""Safe local CRM analytics using fictional records only."""
import json
from pathlib import Path

def build_report(data):
    deals = [d for d in data["deals"] if d["stage"] != "won"]
    pipeline = sum(d["value_gbp"] for d in deals)
    stale = [d for d in deals if d["days_since_activity"] >= 7]
    leads = [x for x in data["leads"] if x["days_since_activity"] >= 4]
    lines = ["# Weekly Sales Meeting Report",
             f"Open pipeline: £{pipeline:,.0f}",
             f"Open opportunities: {len(deals)}",
             f"Deals needing attention: {len(stale)}",
             f"Leads needing follow-up: {len(leads)}",
             "", "## Open deals requiring attention"]
    lines += [f"- {d['name']} — £{d['value_gbp']:,.0f}, last activity {d['days_since_activity']} days ago" for d in stale]
    lines += ["", "## Leads needing follow-up"]
    lines += [f"- {x['name']} — {x['days_since_activity']} days since activity" for x in leads]
    lines += ["", "## Rep activity"]
    for r in data["reps"]:
        lines.append(f"- {r['name']}: {r['calls']} calls, {r['emails']} emails, {r['meetings']} meetings")
    return "\n".join(lines) + "\n"

if __name__ == "__main__":
    data = json.loads((Path(__file__).parent / "sample_crm.json").read_text())
    print(build_report(data))
