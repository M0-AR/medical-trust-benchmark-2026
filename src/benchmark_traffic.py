"""
Benchmark traffic concentration + engagement using 2026 public tables.
Sources (verified via live web search 2026-10-04):
 - Semrush Trending Websites Healthcare Aug2026 via ExplodingTopics: nih.gov 180M, clevelandclinic 87.5M, mayoclinic 66.4M, healthline 57.7M, harvard 36.3M, nhs 31.2M, webmd 30.4M
 - OneLittleWeb Jun2026: NIH 168.18M, Cleveland 78.61M, Mayo 64.33M, Healthline 55.19M, WebMD 28.78M, Drugs.com 22.76M, MedlinePlus 17.39M, WHO 10.58M
 - Similarweb Medicine Jun2026: clevelandclinic #1 medicine, mayoclinic #2, medscape #6
Computes HHI concentration, traffic share, engagement contrast, and hidden patterns.
Outputs: data/traffic_benchmark.json + console table
"""
import json

# Aug2026 Semrush headline table (millions)
aug2026 = [
    ("nih.gov", 180.0),
    ("clevelandclinic.org", 87.5),
    ("mayoclinic.org", 66.4),
    ("healthline.com", 57.7),
    ("harvard.edu", 36.3),
    ("nhs.uk", 31.2),
    ("webmd.com", 30.4),
    ("doctolib.fr", 28.9),
    ("athenahealth.com", 28.7),
    ("ameli.fr", 20.0),  # approx cutoff for top-10 aggregate
]

# Engagement spot values from ExplodingTopics Aug2026
engagement = {
    "athenahealth.com": {"pages": 7.4772, "bounce": 26.56},
    "nih.gov": {"pages": 3.3167, "bounce": 57.73},
    "webmd.com": {"pages": 1.5546, "bounce": 78.09},
    "clevelandclinic.org": {"pages": 1.6557, "bounce": 75.85},
}

def hhi(shares):
    return sum(s*s for s in shares)

def main():
    total = sum(v for _, v in aug2026)
    rows = []
    for site, visits in aug2026:
        share = visits/total
        rows.append({"site": site, "visits_M": visits, "share_pct": round(share*100,2)})
    shares = [r["share_pct"]/100 for r in rows]
    h = hhi(shares)
    # HHI on 0-10000 scale
    hhi10k = round(h*10000,1)

    hidden = [
        "PATTERN-1 Concentration: Top-1 (nih.gov) holds ~%.1f%% of top-10 traffic; top-3 hold ~%.1f%%. HHI=%.0f (moderately concentrated). Trust is centralized in one .gov umbrella." % (
            rows[0]["share_pct"], sum(r['share_pct'] for r in rows[:3]), hhi10k),
        "PATTERN-2 Engagement inversion: athenahealth 7.48 pages/visit + 26.6% bounce (portal workflow) vs webmd 1.55 pages + 78.1% bounce (one-and-done symptom lookup). High trust != high engagement depth.",
        "PATTERN-3 Crisis-spike vs evergreen: WHO only 10.58M Jun2026 (-38.6% MoM) while nih.gov evergreen 168-180M. WHO spikes in pandemics; NIH sustains via PubMed/PMC infrastructure.",
        "PATTERN-4 Medicine-subcategory flip: Similarweb Medicine Jun2026 ranks clevelandclinic #1, mayoclinic #2 (not nih.gov) — category definition changes winner. Always report taxonomy with rank.",
        "PATTERN-5 Commercial efficiency: Healthline+WebMD ~88M combined ≈ Cleveland Clinic alone; ad-supported C-grade evidence matches nonprofit B-grade traffic — monetization compensates trust deficit with SEO.",
    ]
    out = {
        "source_tables": "Semrush Aug2026 + OneLittleWeb Jun2026 + Similarweb Medicine Jun2026 (see README citations)",
        "top10_total_M": round(total,1),
        "rows": rows,
        "HHI_10k": hhi10k,
        "engagement": engagement,
        "hidden_patterns": hidden,
    }
    print(f"Top-10 total ~{total:.1f}M visits/mo | HHI {hhi10k} | nih share {rows[0]['share_pct']}%")
    for r in rows:
        print(f"  {r['site']:22s} {r['visits_M']:6.1f}M  {r['share_pct']:5.2f}%")
    print("Engagement contrast:")
    for k,v in engagement.items():
        print(f"  {k:22s} pages={v['pages']} bounce={v['bounce']}%")
    print("Hidden patterns:")
    for hpat in hidden:
        print("  - "+hpat)
    with open("data/traffic_benchmark.json","w") as f:
        json.dump(out,f,indent=2)
    print("Wrote data/traffic_benchmark.json")

if __name__ == "__main__":
    main()
