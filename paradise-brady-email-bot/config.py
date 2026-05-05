"""Brady's email-bot config. Shared infra in ../../_shared/core."""
import os
import random
import sys
from pathlib import Path

from dotenv import load_dotenv

PROJECT_DIR = Path(__file__).resolve().parent
SHARED_ROOT = PROJECT_DIR.parents[1] / "_shared"
sys.path.insert(0, str(SHARED_ROOT))


def _load_api_key():
    """Look for ANTHROPIC_API_KEY in: env, this bot's .env, shared .env,
    then the Client Website bot's .env (already set up in your dev box)."""
    if os.getenv("ANTHROPIC_API_KEY"):
        return os.getenv("ANTHROPIC_API_KEY")
    candidates = [
        PROJECT_DIR / ".env",
        SHARED_ROOT / ".env",
        Path.home() / "Desktop" / "Client Website email bot" / ".env",
        Path.home() / "Desktop" / "Hermann Email Bot" / ".env",
    ]
    for p in candidates:
        if p.exists():
            load_dotenv(p, override=False)
            if os.getenv("ANTHROPIC_API_KEY"):
                return os.getenv("ANTHROPIC_API_KEY")
    return ""


def _load_app_password():
    if os.getenv("BRADY_GMAIL_APP_PASSWORD"):
        return os.getenv("BRADY_GMAIL_APP_PASSWORD")
    return os.getenv("GMAIL_APP_PASSWORD", "")


API_KEY = _load_api_key()
GMAIL_ADDRESS = "brady@paradisehomedesigninc.com"
GMAIL_APP_PASSWORD = _load_app_password()


def credit_for_tier(tier):
    return {
        "low":   "$2,000",
        "mid":   "$2,000",
        "high":  "$4,000",
        "ultra": "$5,000",
    }.get(tier, "$2,000")


def build_payload_extras(prospect_row):
    """Per-recipient extras the master prompt expects, picked here so the
    bot keeps full control of credit logic and gallery whitelisting."""
    from core import gallery
    tier = prospect_row.get("home_value_tier") or "high"
    town = prospect_row.get("town") or "Lake Forest"
    focus = prospect_row.get("focus_override") or {
        "low": "bathroom", "mid": "kitchen",
        "high": "kitchen", "ultra": "full",
    }.get(tier, "kitchen")
    hero_key, thumb_keys = gallery.pick_for(
        town, focus="kitchen" if focus == "full" else focus,
    )
    return {
        "credit_amount": credit_for_tier(tier),
        "focus": focus,
        "include_ps": random.random() < 0.5,
        "subject_bucket": random.choice([
            "town_specific", "detail_specific",
            "question_style", "personal",
        ]),
        "available_gallery_keys": [hero_key] + thumb_keys,
        "suggested_hero": hero_key,
        "suggested_thumbs": thumb_keys,
    }
