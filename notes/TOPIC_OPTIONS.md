# Working thesis options — decision pending

These are discussion proposals, **not formally approved thesis titles**.

| Option | Draft question | Practical component | Risks | Fit |
|---|---|---|---|---|
| A. Network intrusion detection | Can standard ML models identify attacks in network-flow data, and how robust is their evaluation? | Python (pandas, scikit-learn), public dataset, model comparison, clear metrics | Leakage, dataset realism, class imbalance | Best supported by current sources |
| B. Phishing URL detection | Can interpretable lexical URL features detect phishing, and how does performance change on held-out domains or later samples? | Feature extractor, logistic regression / random forest, small demo | Reliable labeling, overlapping sources, temporal drift | A focused, feasible alternative |
| C. Ransomware behavioral detection | Which observable file/process behaviors best distinguish ransomware-like activity from benign actions? | Safe, non-malicious simulation or published traces; defensive detector | Access to trustworthy behavioral traces; safe experiment scope | Interesting, but needs targeted literature |

## Suggested conversation with supervisor

- Is a comparative empirical project an adequate bachelor's-thesis contribution?
- Which of A / B / C suits expected difficulty and timeframe?
- Should the work emphasize explainability, reproducibility, performance, or practical implementation?
- Which datasets and ethical restrictions apply?
- How many papers are expected for the *first* review versus final thesis?

## Recommendation for discussion

Lead with **A** as a working research area while openly stating topic flexibility. If a narrowly scoped Python application is preferred, propose **B**. Keep **C** exploratory pending additional evidence.

No code, dataset experiments or literature-analysis results have been produced yet.
