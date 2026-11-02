# Sales Intelligence & Rep Activity Tracker

> **Offline demonstration** using fictional CRM opportunities, leads and sales representative activity. Not a replica of an employer's internal reporting bots.

This small Python application generates a readable weekly sales meeting brief showing open pipeline, deals needing attention, leads without recent follow-up and rep activity totals.

## Run
Requires Python 3.10+, standard library only.

```bash
python report.py
python -m unittest discover -s tests -v
```

## What the demo covers
- Open pipeline calculations, excluding deals marked won or lost
- Deals with no activity for at least 7 days
- Leads with no activity for at least 4 days
- Calls, emails and meetings by rep
- Four automated tests and GitHub Actions CI

All monetary values, contacts and performance figures in `sample_crm.json` are fictional.

## Next steps
Add a permissioned HubSpot/CRM adapter, durable snapshots, scheduled report delivery and reviewed AI-generated commentary.

**Important distinction:** The code currently published here **does not call Grok**. The title reflects the professional project theme; an optional xAI/Grok integration is a future extension, not a demonstrated feature in this repository. Never upload confidential CRM data or API keys.
