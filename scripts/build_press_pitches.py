"""Write one press pitch draft per state with the highest median hospital markup.

Run where the real database is: python scripts/build_press_pitches.py
Every number comes from the ranking page's own data, so the pitch and the page agree.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config  # noqa: E402
from hospital_rankings import get_ranked_state_slugs, get_state_ranking  # noqa: E402

PITCH_TEMPLATE = """# Pitch: {state_name}

To: [reporter name], [outlet] (health or consumer desk)
Subject: Hospital list prices in {state_name} run a median {median:.1f}x what Medicare pays

Hi [first name],

I compared {ranked_count} {state_name} hospitals' published prices with what Medicare pays for the same procedures. The median hospital's list prices run {median:.1f}x Medicare. The highest is {top_name} in {top_city} at {top_markup:.1f}x; the lowest of the ranked hospitals is {low_name} in {low_city} at {low_markup:.1f}x.

The full ranking, with each hospital's figure, is here: {url}

The method: each hospital's price for the same set of procedures (at least {min_procedures} per hospital) divided by the Medicare rate for the same billing code, averaged. List prices are not what insured patients pay, and the page says so. The data is from hospitals' own price files and CMS, as of {as_of}.

I'm happy to send the underlying numbers or a county-level cut for your coverage area.

[your name]
BillKarma, billkarma.app
"""


def build_pitches(output_dir: str = config.PITCH_OUTPUT_DIR) -> list[str]:
    rankings = [get_state_ranking(slug) for slug in get_ranked_state_slugs()]
    rankings = [r for r in rankings if r]
    rankings.sort(key=lambda r: r["median_markup"], reverse=True)
    os.makedirs(output_dir, exist_ok=True)
    paths = []
    for ranking in rankings[: config.PITCH_STATE_COUNT]:
        top = ranking["most_expensive"][0]
        low = ranking["most_expensive"][-1] if not ranking["least_expensive"] else ranking["least_expensive"][0]
        text = PITCH_TEMPLATE.format(
            state_name=ranking["state_name"],
            median=ranking["median_markup"],
            ranked_count=ranking["ranked_count"],
            top_name=top["name"], top_city=top["city"], top_markup=top["markup"],
            low_name=low["name"], low_city=low["city"], low_markup=low["markup"],
            url=f"{config.APP_URL.rstrip('/')}/hospitals/{ranking['state_slug']}/most-expensive/",
            min_procedures=config.RANKING_MIN_PROCEDURES,
            as_of=ranking["as_of"] or "the latest data refresh",
        )
        path = os.path.join(output_dir, f"{ranking['state_slug']}.md")
        with open(path, "w") as f:
            f.write(text)
        paths.append(path)
    return paths


if __name__ == "__main__":
    written = build_pitches()
    print(f"Wrote {len(written)} pitches" if written else "No state has enough ranked hospitals yet")
    for path in written:
        print(path)
