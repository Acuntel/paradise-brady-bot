"""Generate Brady's test previews without hitting the live API.
Each sample follows MASTER_PROMPT.md exactly: ASCII hyphens only, no em
dashes, no banned words, body cap 130 words, full signoff block."""
import sys
from pathlib import Path

SHARED_ROOT = Path(__file__).resolve().parents[2] / "_shared"
sys.path.insert(0, str(SHARED_ROOT))

from core import make_samples  # noqa: E402

import run as bot_run  # noqa: E402


SIGNOFF = (
    "- Brady Schwartz\n"
    "Paradise Home Design Inc\n"
    "brady@paradisehomedesigninc.com\n"
    "See our work: paradisehomedesigninc.com/gallery.html"
)
PS = "P.S. if your spouse is the one who'd care, feel free to forward this."


SAMPLES = [
    {
        "subject": "Quick one about your kitchen",
        "body_text": (
            "Hi Sarah, I'm Brady. I'm 18 and just started in sales at "
            "Paradise Home Design over on Deerpath in Lake Forest. "
            "Congrats on the new place. This is my first real job and "
            "I'm trying to prove I can actually bring in work, so I'm "
            "writing personally to a handful of homes in Highland Park.\n\n"
            "Paradise has been doing kitchens and baths up here for 38 "
            "years, and they gave me a $4,000 credit I can put toward any "
            "remodel booked this month. That's on top of a free in-home "
            "estimate with sketches and real numbers, no pressure.\n\n"
            "We carry Adelphi and Medallion through our Deerpath showroom, "
            "and the team is BBB-accredited and insured.\n\n"
            "If updating the kitchen has been on your list, our designer "
            "can come measure and put real numbers on it. Worth a 15-minute "
            "walkthrough this week or next?\n\n"
            f"{SIGNOFF}\n\n{PS}"
        ),
        "hero_key": "kitchen_white_pendants",
        "thumb_keys": ["kitchen_marble_brass", "kitchen_white_modern", "bath_double_vanity"],
        "fname": "01_sarah_highland_park.html",
    },
    {
        "subject": "From your neighbor in Lake Forest",
        "body_text": (
            "Hi Marcus, I'm Brady. I'm 18 and this is my first real sales "
            "job, at Paradise Home Design on Deerpath here in Lake Forest. "
            "I'm reaching out personally to a few homes in Winnetka.\n\n"
            "Paradise has been doing kitchens and baths on the North Shore "
            "for 38 years. They gave me a $5,000 credit I can put toward "
            "any kitchen or primary bath booked this month, on top of a "
            "free in-home estimate with sketches and real numbers, no "
            "pressure.\n\n"
            "Our showroom on Deerpath is open if you'd rather walk through "
            "cabinet samples in person first. The team is fully insured "
            "and we bring copies before any work starts.\n\n"
            "If the kitchen or primary bath has been on the list, our "
            "designer can come to you. Worth 15 minutes Tuesday or "
            "Thursday evening?\n\n"
            f"{SIGNOFF}"
        ),
        "hero_key": "kitchen_marble_arch",
        "thumb_keys": ["kitchen_marble_brass", "kitchen_black_island", "kitchen_white_pendants"],
        "fname": "02_marcus_winnetka.html",
    },
    {
        "subject": "Working in Vernon Hills this month",
        "body_text": (
            "Hi David, I'm Brady. I'm 18 and just started in sales at "
            "Paradise Home Design in Lake Forest. This is my first real "
            "job, and I'm writing personally to a handful of homes in "
            "Vernon Hills.\n\n"
            "Paradise has been doing kitchens in this area for 38 years, "
            "and they gave me a $2,000 credit I can put toward any "
            "kitchen booked this month. That's on top of a free in-home "
            "estimate with sketches and real numbers, no pressure.\n\n"
            "We carry Fabuwood and Medallion cabinetry through our "
            "Deerpath showroom, and the install team is BBB-accredited.\n\n"
            "If the kitchen has been on your list, our designer can come "
            "measure and put real numbers on it. Worth a 15-minute "
            "walkthrough this week or next?\n\n"
            f"{SIGNOFF}\n\n{PS}"
        ),
        "hero_key": "kitchen_traditional_cream",
        "thumb_keys": ["kitchen_navy_island_small", "kitchen_white_modern", "kitchen_white_pendants"],
        "fname": "03_david_vernon_hills.html",
    },
    {
        "subject": "First job, hoping for a shot",
        "body_text": (
            "Hi Jennifer, I'm Brady. I'm 18 and this is my first real "
            "sales job, working for Paradise Home Design on Deerpath in "
            "Lake Forest. I'm writing personally to a few homes in town.\n\n"
            "Paradise has been on Deerpath for 38 years, and they gave "
            "me a $5,000 credit I can put toward any kitchen or primary "
            "bath booked this month. That's on top of a free in-home "
            "estimate with sketches and real numbers, no pressure.\n\n"
            "Our showroom is open if you'd rather walk through cabinet "
            "and stone samples in person first. We see a lot of homes "
            "from your home's era due for an updated kitchen or bath.\n\n"
            "Worth a 15-minute walkthrough Tuesday or Thursday evening?\n\n"
            f"{SIGNOFF}"
        ),
        "hero_key": "kitchen_marble_brass",
        "thumb_keys": ["kitchen_marble_arch", "kitchen_black_island", "kitchen_white_modern"],
        "fname": "04_jennifer_lake_forest.html",
    },
    {
        "subject": "A thought on your bath",
        "body_text": (
            "Hi Tom, I'm Brady. I'm 18 and just started in sales at "
            "Paradise Home Design in Lake Forest. This is my first real "
            "job and I'm writing personally to a handful of homes in "
            "Buffalo Grove.\n\n"
            "Paradise has been doing baths in this area for 38 years, "
            "and they gave me a $2,000 credit I can put toward any "
            "primary bath booked this month, on top of a free in-home "
            "estimate with sketches and real numbers, no pressure.\n\n"
            "We carry Florida Tile, Casabella, and Schaub hardware "
            "through our Deerpath showroom. We see a lot of baths from "
            "your home's era due for a refresh.\n\n"
            "Worth 15 minutes for our designer to swing by this week "
            "or next?\n\n"
            f"{SIGNOFF}\n\n{PS}"
        ),
        "hero_key": "bath_double_vanity",
        "thumb_keys": ["kitchen_traditional_cream", "kitchen_white_modern", "kitchen_white_pendants"],
        "fname": "05_tom_buffalo_grove.html",
    },
    {
        "subject": "Open to a 15-minute walkthrough?",
        "body_text": (
            "Hi Linda, I'm Brady. I'm 18 and just started in sales at "
            "Paradise Home Design in Lake Forest. Congrats on the new "
            "place in Glencoe. This is my first real job and I'm writing "
            "personally to a few homes in town.\n\n"
            "Paradise has been doing kitchens and baths on the North "
            "Shore for 38 years, and they gave me a $4,000 credit I can "
            "put toward any kitchen or primary bath booked this month. "
            "That's on top of a free in-home estimate with sketches and "
            "real numbers, no pressure.\n\n"
            "We carry Adelphi, Candlelight, and Fabuwood through our "
            "open showroom on Deerpath.\n\n"
            "If you've been thinking about updating the kitchen, our "
            "designer can come to you. Worth a 15-minute walkthrough "
            "Tuesday or Thursday evening?\n\n"
            f"{SIGNOFF}"
        ),
        "hero_key": "kitchen_marble_brass",
        "thumb_keys": ["kitchen_marble_arch", "kitchen_white_chandeliers", "kitchen_white_pendants"],
        "fname": "06_linda_glencoe.html",
    },
]


if __name__ == "__main__":
    paths = make_samples.generate(bot_run.CFG, SAMPLES)
    for p in paths:
        print("wrote", p)
