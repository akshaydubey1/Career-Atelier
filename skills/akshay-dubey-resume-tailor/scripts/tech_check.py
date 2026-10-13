#!/usr/bin/env python3
"""Resume Tailor by Akshay Dubey (MIT). Check that every technology placed in a role existed during that role.

Usage: python tech_check.py roles.json
roles.json: [{"role": "Lead DevOps Engineer, CGI", "start": 2019, "end": 2024, "tech": ["EKS", "Argo CD", ...]}, ...]
Use the current year for "end" when the role is ongoing. Exit code 1 if any FAIL.
"""
import json, sys
from pathlib import Path

TIMELINE = Path(__file__).resolve().parent.parent / "references" / "tech-timeline.json"


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    years = {k: v for k, v in json.loads(TIMELINE.read_text()).items() if not k.startswith("_")}
    roles = json.loads(Path(sys.argv[1]).read_text())
    fails = warns = 0
    unknown = set()
    for r in roles:
        start, end = int(r["start"]), int(r["end"])
        for t in r.get("tech", []):
            y = years.get(t.strip().lower())
            if y is None:
                unknown.add(t)
            elif y > end:
                fails += 1
                print(f"FAIL  {t} (first released {y}) is in '{r['role']}' ({start}-{end})")
            elif y == end and start < end:
                warns += 1
                print(f"CHECK {t} (first released {y}) appears only in the final year of '{r['role']}' ({start}-{end})")
    if unknown:
        print("UNKNOWN (verify release year yourself): " + ", ".join(sorted(unknown)))
    print(f"{fails} fail, {warns} to check")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
