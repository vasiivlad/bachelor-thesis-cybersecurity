# Source-by-source notes (preliminary)

**IMPORTANT:** These are **screening notes based on abstracts and accessible source descriptions**, not a claim of complete critical reading. Revisit each source, check methodological detail and add page numbers before submitting as an in-depth literature review.

## 1. Khraisat et al. (2019) — `khraisat2019survey`
**What it covers:** Survey and categorization of signature-based and anomaly-based intrusion detection; datasets and attack evasion issues.
**Useful for thesis:** Introductory definition of IDS, comparison of paradigms, and a map of challenges to motivate why detection performance must be tested critically.
**Possible section:** Background / Related work.
**Question for full read:** Which evaluation limitations are still open in recent work?
**Limitations:** Survey reflects literature up to 2019; must complement with recent studies.

## 2. Ring et al. (2019) — `ring2019survey`
**What it covers:** Comparison of network intrusion detection datasets using systematic dataset properties.
**Useful for thesis:** Helps justify dataset choice instead of selecting a popular benchmark without checking recording conditions, labels, capture and representativeness.
**Possible section:** Data selection / Experimental methodology.
**Question for full read:** Which listed datasets permit realistic train/test splits?
**Limitations:** Older survey; assess changes to datasets and later criticisms.

## 3. Sharafaldin et al. (2018) — `sharafaldin2018dataset`
**What it covers:** Design and characterization of CICIDS2017 with benign and malicious network traffic scenarios, extraction of flow features, and experiments.
**Useful for thesis:** Primary source documenting a potential experimental dataset. Useful for dataset composition, feature interpretation and baselines.
**Possible section:** Dataset and preprocessing.
**Question for full read:** What scenario, day, attack, labeling, and feature issues could bias experiments?
**Limitations:** Performance on a benchmark does not establish production effectiveness; check later critiques and leakage risk.

## 4. Sommer & Paxson (2010) — `sommer2010outside`
**What it covers:** Why machine learning systems for network IDS can struggle when moved from constrained research environments to operational networks.
**Useful for thesis:** Justification for reporting false positives, generalization and threats to validity rather than accuracy alone.
**Possible section:** Motivation / Limitations / Evaluation design.
**Question for full read:** What assumptions distinguish closed-world benchmarks from open-world detection?
**Limitations:** Early work, primarily conceptual; use newer evidence when choosing current methods.

## 5. Sahingoz et al. (2019) — `sahingoz2019phishing`
**What it covers:** Feature engineering and machine-learning classification for phishing URLs using lexical and NLP-related signals.
**Useful for thesis:** Foundation for an alternative practical thesis with a supervised classifier and accessible inputs, without network packet analysis.
**Possible section:** Phishing background / Related work / Features.
**Question for full read:** Is the evaluation robust against duplicates, changing URLs, domain overlap and temporal leakage?
**Limitations:** Publisher PDF may require university access; results may not generalize to current phishing campaigns.

## Comparative synthesis

- **IDS route:** Khraisat provides taxonomy; Ring helps select data; Sharafaldin documents CICIDS2017; Sommer & Paxson warns against weak evaluation.
- **Phishing route:** Sahingoz establishes a baseline framing, but a dedicated, more recent collection of phishing papers is necessary.
- **Ransomware route:** Not yet backed by enough literature in this collection. Keep as tentative only.

## Annotation template for next paper

- Reference key and complete citation:
- Full-text status / version / date accessed:
- Research question:
- Dataset and experimental design:
- Main reported findings (with page/figure):
- Method strengths:
- Limitations / possible bias:
- Relevance to **my** thesis:
- What I would adapt or challenge:
- 2–3 exact page-specific citations:
