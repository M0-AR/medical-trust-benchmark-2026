# PhD Roadmap — Six Publishable Extensions of the Medical Trust Benchmark

Each extension below is scoped as a standalone publishable paper building directly on `data/*.json` in this repo. For each: hypothesis, method, data, evaluation, venue, and falsification criterion.

## P1 — Longitudinal Trust Dynamics (WHO crisis-spike vs NIH evergreen)

- **Hypothesis:** WHO traffic Granger-causes GDELT news volume; NIH traffic follows academic calendar, not news.
- **Method:** Cron daemon hourly: portal liveness + SimilarWeb/Tranco ranks + GDELT news counts for 90 days. Time-series decomposition + Granger test.
- **Data:** This repo's `verify_trust.py` extended with scheduler + `data/longitudinal/*.jsonl`.
- **Eval:** p-values, impulse-response, pre-registered event list (outbreak declarations).
- **Venue:** J Med Internet Res.
- **Falsify if:** WHO/NIH correlation difference < 0.2 or Granger p > 0.05 both ways.

## P2 — Taxonomy Instability Audit

- **Hypothesis:** Category definition elects the winner (nih.gov vs clevelandclinic.org flip).
- **Method:** Daily scrape Semrush/Similarweb/OneLittleWeb taxonomies; rank-biased overlap (RBO) across taxonomies; report instability index.
- **Venue:** Nature Digital Medicine (Comment/Analysis).
- **Falsify if:** RBO > 0.9 across taxonomies for 30 consecutive days.

## P3 — Human DISCERN Trial (proxy-human gap)

- **Hypothesis:** Automated JAMA homepage proxy correlates poorly (ρ < 0.4) with human DISCERN on treatment articles.
- **Method:** 2 trained raters × 50 treatment articles × 10 portals; DISCERN-16 + JAMA-4 + HONcode checklist; Cohen κ; Spearman proxy-human.
- **Venue:** BMJ Health & Care Informatics.
- **Falsify if:** ρ ≥ 0.6 (proxy is better than claimed).

## P4 — Delisting Early Warning (Scopus/WoS 2025 labels)

- **Hypothesis:** Volume surge + self-cite rate + board churn predicts removal 6 months ahead (AUC > 0.8).
- **Method:** Features from OpenAlex/Crossref (volume slope, self-cite, SJR/CiteScore trend) on 56 Scopus + 128 WoS 2025 removals vs matched controls; XGBoost + temporal split.
- **Venue:** Quantitative Science Studies.
- **Falsify if:** AUC < 0.7 on held-out 2026 removals.

## P5 — China–West Coverage Gap

- **Hypothesis:** ≥30% of high-quality Chinese surgical/device trials (SinoMed/CNKI) are invisible to PubMed.
- **Method:** Paired queries: English MeSH vs Chinese subject headings; compare recall; map ChiCTR↔NCT via ICTRP; quantify invisible set + citation loss.
- **Venue:** Lancet Digital Health.
- **Falsify if:** Overlap recall > 90%.

## P6 — Cost-Aware Federated Scholarly Search

- **Hypothesis (seeded by Pattern-6):** Date-filtered OpenAlex conjunctive queries cost >3× bare search; a planner routing PubMed/Crossref/ClinicalTrials by query shape cuts p95 latency 40% at equal recall.
- **Method:** Benchmark matrix (query shape × API × latency/recall); learn router; evaluate on 200 sampled systematic-review questions.
- **Venue:** JAMIA.
- **Falsify if:** No planner beats round-robin by >10% p95.

## General PhD method checklist (2026–2027 standard)

1. Pre-register hypotheses + falsification thresholds (this file is the pre-registration).
2. Sequential polite fetching, backoff, negatives logged.
3. Docker + pinned requirements + data timestamps for every figure.
4. Human subjects (P3): IRB + rater training logs + κ reporting.
5. China work (P5): bilingual protocol + firewall vantage disclosure.
6. All code + data public; vendor tables cited with access date (2026-10-04).
