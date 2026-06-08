"""Build a real job-postings classroom sample from a public dataset.

Source: `xanderios/linkedin-job-postings` on the Hugging Face Hub. This is a
no-login mirror of the same Kaggle "LinkedIn Job Postings (2023-2024)" dataset
that the Week 6 README cites. We read rows through the public
datasets-server JSON API (no auth, standard library only), filter to
tech/data roles, map columns onto the Week 6 schema, and write a small,
deterministic CSV for use in the lessons and the capstone template.

Run:
    python week_06/scripts/build_job_postings_sample.py

Output:
    week_06/data/sample_job_postings.csv   (~60 real rows)

The output is intentionally small (a classroom sample). For a stronger final
project, download a larger prepared subset yourself and follow the dataset's
license/terms.
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

DATASET = "xanderios/linkedin-job-postings"
ROWS_API = "https://datasets-server.huggingface.co/rows"

# Target schema used across Week 6 lessons and the capstone template.
SCHEMA = [
    "job_id",
    "job_title",
    "company",
    "location",
    "job_description",
    "job_skills",
    "posted_date",
    "source",
]

# Keep tech/data roles so the "skill analyzer / learning path" theme is relevant.
TITLE_KEYWORDS = (
    "data",
    "engineer",
    "analyst",
    "developer",
    "scientist",
    "machine learning",
    "ml ",
    "software",
    "devops",
    "ai ",
    "ai/",
    "programmer",
)

TARGET_ROWS = 60
PAGE_SIZE = 100
MAX_OFFSET = 4000  # scan budget; tech roles are a fraction of all rows
DESCRIPTION_MAX_CHARS = 1500


def fetch_page(offset: int, length: int) -> list[dict]:
    """Fetch one page of rows from the datasets-server API."""
    params = urllib.parse.urlencode(
        {
            "dataset": DATASET,
            "config": "default",
            "split": "train",
            "offset": offset,
            "length": length,
        }
    )
    url = f"{ROWS_API}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "week06-sample-builder"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = json.load(resp)
    return [item["row"] for item in payload.get("rows", [])]


def looks_techy(title: str) -> bool:
    low = f" {title.lower()} "
    return any(kw in low for kw in TITLE_KEYWORDS)


def epoch_ms_to_date(value) -> str:
    try:
        ms = float(value)
    except (TypeError, ValueError):
        return ""
    return dt.datetime.fromtimestamp(ms / 1000.0, dt.timezone.utc).strftime("%Y-%m-%d")


def clean_text(value) -> str:
    if value is None:
        return ""
    text = str(value).replace("\r\n", "\n").strip()
    # Collapse runs of blank lines/whitespace so the CSV stays compact.
    text = " ".join(text.split())
    return text


def map_row(row: dict) -> dict | None:
    title = clean_text(row.get("title"))
    description = clean_text(row.get("description"))
    if not title or not description:
        return None
    if not looks_techy(title):
        return None
    if len(description) > DESCRIPTION_MAX_CHARS:
        description = description[: DESCRIPTION_MAX_CHARS - 1].rstrip() + "…"
    return {
        "job_id": row.get("job_id", ""),
        "job_title": title,
        "company": "",  # HF mirror only carries company_id, not a name
        "location": clean_text(row.get("location")),
        "job_description": description,
        "job_skills": clean_text(row.get("skills_desc")),
        "posted_date": epoch_ms_to_date(row.get("listed_time")),
        "source": "linkedin_kaggle_2023_2024",
    }


def main() -> None:
    out_path = Path(__file__).resolve().parents[1] / "data" / "sample_job_postings.csv"

    collected: list[dict] = []
    seen_ids: set = set()
    offset = 0
    while len(collected) < TARGET_ROWS and offset < MAX_OFFSET:
        rows = fetch_page(offset, PAGE_SIZE)
        if not rows:
            break
        for row in rows:
            mapped = map_row(row)
            if mapped is None:
                continue
            if mapped["job_id"] in seen_ids:
                continue
            seen_ids.add(mapped["job_id"])
            collected.append(mapped)
            if len(collected) >= TARGET_ROWS:
                break
        offset += PAGE_SIZE
        print(f"  scanned offset {offset}, collected {len(collected)}", file=sys.stderr)

    if not collected:
        raise SystemExit("No rows collected; the API may have changed or be unreachable.")

    with out_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=SCHEMA)
        writer.writeheader()
        writer.writerows(collected)

    print(f"Wrote {len(collected)} rows to {out_path}")


if __name__ == "__main__":
    main()
