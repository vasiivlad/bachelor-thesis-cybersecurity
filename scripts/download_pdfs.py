#!/usr/bin/env python3
"""Fetch accessible research PDFs. Review license before redistributing."""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "literature" / "pdfs"
DEST.mkdir(parents=True, exist_ok=True)

SOURCES = {
    "khraisat2019survey.pdf": "https://cybersecurity.springeropen.com/counter/pdf/10.1186/s42400-019-0038-7.pdf",
    "ring2019survey_preprint.pdf": "https://arxiv.org/pdf/1903.02460",
    "sharafaldin2018dataset.pdf": "https://www.scitepress.org/PublishedPapers/2018/66398/pdf/index.html",
    "sommer2010outside.pdf": "https://gangw.cs.illinois.edu/class/cs562/papers/Closed_World-IDS-sp10.pdf",
}

for filename, url in SOURCES.items():
    output = DEST / filename
    if output.exists():
        print(f"SKIP {filename}: already exists")
        continue
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0 academic literature collection"})
        with urlopen(req, timeout=30) as response:
            data = response.read()
        if not data.startswith(b"%PDF-"):
            print(f"FAIL {filename}: server returned non-PDF content")
            continue
        output.write_bytes(data)
        print(f"OK   {filename} ({len(data):,} bytes)")
    except (URLError, HTTPError, TimeoutError, OSError) as exc:
        print(f"FAIL {filename}: {exc}")

print("Remaining source: Sahingoz 2019; check university institutional access.")
print("Before redistributing downloaded PDFs, verify each paper's license.")
