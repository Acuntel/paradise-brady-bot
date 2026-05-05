# Brady's Paradise Email Bot

## What this is

Cold-outreach bot for **Paradise Home Design Inc.** signed by **Brady Schwartz**
(brady@paradisehomedesigninc.com). High-school-student-on-his-first-sales-job
angle. Targets homeowners in 1-hour radius of Lake Forest with a tiered
neighborhood credit ($2k / $4k / $5k by home value) and a free in-home
estimate.

## Pitch contract

See `MASTER_PROMPT.md`. Body cap 130 words, ASCII hyphens only, no AI jargon
words, no em dashes, ever.

## Sender

- Name: Brady Schwartz
- Email: brady@paradisehomedesigninc.com (Workspace inbox; needs an App Password
  for IMAP draft uploads)
- Sign-off: "- Brady Schwartz / Paradise Home Design Inc / [email] / See our work: paradisehomedesigninc.com/gallery.html"

## Commands

```bash
# Ingest test prospects
python run.py load data/sample_leads.csv

# MX-verify (no Hunter, no paid APIs)
python run.py verify

# Generate previews and pop them in Safari (no Gmail draft created)
python run.py preview 6

# Generate real Gmail drafts (requires GMAIL_APP_PASSWORD in .env)
python run.py draft 50
```

## Architecture

Imports from `../../_shared/core/`:

- `verifier.py` - MX-only check
- `scraper.py` - DDGS + BS4 (no Hunter, no Apollo)
- `tracker.py` - per-bot SQLite + shared dedupe DB at `../../_shared/data/dedupe.db`
- `generator.py` - Claude API call with prompt caching
- `html_template.py` - warm HTML with hero, body, 3-thumb gallery, footer
- `sender.py` - Gmail IMAP draft creator
- `runner.py` - the CLI pipeline

This bot's local code:

- `config.py` - sender identity, credit tiers, gallery whitelist
- `MASTER_PROMPT.md` - the immutable copy contract
- `data/sample_leads.csv` - test prospects (replace with real sourced leads)

## Safety rails

1. Draft-first - never sends unless you push from Gmail Drafts.
2. Cross-bot dedupe via shared `dedupe.db`. No homeowner gets two Paradise emails.
3. Bounce kill: any bounce flips do_not_contact=1 forever.
4. STOP kill: handled out-of-band (read replies, run `add_dnc`).
5. 130-word body cap, banned-word list enforced, em dashes auto-reject.

## Credit tiers (filled in by the bot before Claude generates)

| home_value_tier         | credit_amount |
| ----------------------- | ------------- |
| low / mid (under $1.5M) | $2,000        |
| high ($1.5M - $3M)      | $4,000        |
| ultra ($3M+)            | $5,000        |
