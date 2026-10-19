# Bachelor's thesis — literature review (exploratory)

**Status:** Initial literature collection, 19 October 2026. **Topic not finalized.**

This project prepares the first supervisor meeting and explores three related directions:
1. Network intrusion detection and analysis (strong candidate)
2. Machine-learning-based phishing URL detection (smaller, focused option)
3. Ransomware or malware behavioral detection (candidate requiring more literature)

The included readings are **starting points**, not claims that the papers have been read in full. Notes are based on publisher abstracts and available paper text. Read the full papers, add page numbers, and revise the judgments before treating this as a completed critical literature review.

## Supervisor's requested deliverables

- [x] Curated relevant literature with DOI / publisher / PDF links (see `literature/SOURCES.md`)
- [x] Preliminary notes for each considered paper (`notes/LITERATURE_NOTES.md`)
- [x] Bibliographic metadata (`references.bib`)
- [ ] Download and check source PDFs in `literature/pdfs/`
- [ ] Read and annotate full papers, add page-specific references
- [ ] Decide exact research question with supervisor

## Repository layout

```
thesis-research/
  README.md
  references.bib
  literature/
    SOURCES.md
    pdfs/README.md
  notes/
    LITERATURE_NOTES.md
    TOPIC_OPTIONS.md
    MEETING_BRIEF.md
  scripts/
    download_pdfs.py
```

## Possible thesis: intrusion detection

**Draft question:** How accurately can basic machine learning methods detect malicious network flows in a public intrusion detection dataset, and what are their limitations?

**Tentative experiment:** Explore CICIDS2017; clean and split data correctly; compare logistic regression/random forest with simple baseline; report precision, recall, F1, confusion matrix, false positives, and class imbalance. No method has been implemented yet.

**Why start here?** There is an accessible academic foundation, defined data sources and a measurable evaluation task. The experimental scope needs approval.

## Downloading PDFs

Run `python3 scripts/download_pdfs.py` from the `thesis-research` directory. This fetches freely hosted PDFs where a direct link is identified. It does not download paywalled articles or bypass permissions. Verify each PDF matches the cited version; check authors and titles.

## Academic integrity and progress

Do not present preliminary summaries as original reading notes. Some papers require institutional access; links are provided instead of claiming they are stored locally. Proper attribution is tracked in `references.bib`.

## Next steps

1. Discuss preferred direction and manageable project scope.
2. Download readable PDFs and read 2–3 starting papers.
3. Extend per-paper notes with methods, evidence, limitations, exact pages.
4. Search 2023–2026 follow-up literature in the chosen niche.
5. Agree on a dataset, baseline, evaluation plan, and milestone.
