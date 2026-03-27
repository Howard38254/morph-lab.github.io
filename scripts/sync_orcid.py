#!/usr/bin/env python3
"""
Sync publications from ORCID public API to _data/publications.json.

Usage:
    python scripts/sync_orcid.py

Environment variables:
    ORCID_ID  - ORCID iD to fetch (default: 0000-0002-8219-8983)
    OUTPUT    - Output file path (default: _data/publications.json)
"""

import json
import os
import sys
import urllib.request
import urllib.error

ORCID_ID = os.environ.get("ORCID_ID", "0000-0002-8219-8983")
OUTPUT_FILE = os.environ.get("OUTPUT", "_data/publications.json")
ORCID_API = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "morph-lab-site/1.0 (https://morph-lab.github.io)",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def extract_doi(external_ids: list) -> str:
    for eid in external_ids or []:
        if eid.get("external-id-type") == "doi":
            val = eid.get("external-id-value", "")
            # Normalize: strip leading https://doi.org/
            val = val.replace("https://doi.org/", "").replace("http://doi.org/", "")
            return val
    return ""


def extract_url(external_ids: list) -> str:
    for eid in external_ids or []:
        url = eid.get("external-id-url", {})
        if isinstance(url, dict):
            val = url.get("value", "")
            if val:
                return val
    return ""


def parse_works(data: dict) -> list:
    publications = []
    seen_titles = set()

    for group in data.get("group", []):
        summaries = group.get("work-summary", [])
        if not summaries:
            continue

        # Use the first (preferred) summary
        s = summaries[0]

        title_obj = s.get("title", {}) or {}
        title = (title_obj.get("title") or {}).get("value", "").strip()
        if not title or title in seen_titles:
            continue
        seen_titles.add(title)

        pub_date = s.get("publication-date") or {}
        year_obj = pub_date.get("year") or {}
        year = year_obj.get("value", "") if isinstance(year_obj, dict) else ""

        journal_obj = s.get("journal-title") or {}
        journal = journal_obj.get("value", "") if isinstance(journal_obj, dict) else ""

        work_type = s.get("type", "")

        ext_ids = (s.get("external-ids") or {}).get("external-id", [])
        doi = extract_doi(ext_ids)
        url = extract_url(ext_ids)

        # Try to extract authors from the work (only in full work, not summary)
        # For summaries we don't have author info; leave blank for now
        authors = ""

        pub = {
            "title": title,
            "authors": authors,
            "journal": journal,
            "year": year,
            "type": work_type,
            "doi": doi,
            "url": url,
        }
        publications.append(pub)

    # Sort by year descending, then title
    def sort_key(p):
        try:
            return (-int(p.get("year") or 0), p.get("title", ""))
        except (ValueError, TypeError):
            return (0, p.get("title", ""))

    publications.sort(key=sort_key)
    return publications


def main():
    print(f"Fetching works for ORCID {ORCID_ID} ...")
    try:
        data = fetch_json(ORCID_API)
    except urllib.error.HTTPError as e:
        print(f"ERROR: HTTP {e.code} fetching ORCID data: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: URL error fetching ORCID data: {e.reason}", file=sys.stderr)
        sys.exit(1)

    publications = parse_works(data)
    print(f"Found {len(publications)} publications.")

    os.makedirs(os.path.dirname(OUTPUT_FILE) if os.path.dirname(OUTPUT_FILE) else ".", exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(publications, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
