# EigenValue — CritPt frontier-physics reproduction & new-challenge workbench

A study of **[CritPt](https://arxiv.org/abs/2509.26574)** — *Complex Research using Integrated
Thinking, Physics Test* — a benchmark of 71 research-level physics challenges with
**guess-resistant, machine-verifiable answers**, on which the best LLM scores only ~10%.

This repo does three things, starting from an analysis of CritPt's 70 public challenges:

1. **Analyzes** every public challenge → subfield + most-relevant paper
   ([`docs/`](docs/), English + Chinese).
2. **Reproduces three challenges end-to-end** from first principles, each validated against
   known limits ([`critpt_repro/REPRODUCTIONS.md`](critpt_repro/REPRODUCTIONS.md)).
3. **Authors six new challenges** in the exact CritPt format, with every answer computed and
   verified ([`critpt_repro/NEW_CRITPT_QUESTIONS.md`](critpt_repro/NEW_CRITPT_QUESTIONS.md)).

> The public CritPt set ships its reference answers **blanked out** (held-out grading), so every
> number below was derived independently and cross-checked — never copied from the benchmark.

---

## 1 · Subfield & paper analysis

[`docs/subfield_paper_analysis.en.md`](docs/subfield_paper_analysis.en.md) (English) /
[`docs/subfield_paper_analysis.md`](docs/subfield_paper_analysis.md) (Chinese) map all 70 public
challenges to a subfield and their nearest-neighbour reference paper, across condensed matter,
high-energy/gravity/QCD, quantum information, AMO/optics/metrology, and statistical/fluid/
biophysics. Low-confidence matches are flagged explicitly.

## 2 · Three reproductions

| Challenge | Subfield | Method | Result (independently derived) |
|---|---|---|---|
| **#17 SYK zero-T entropy** | High-energy / CMT | Maldacena–Stanford closed form + finite-N ED | **S/N = 0.2324** |
| **#31 Rayleigh–Bénard, mixed BCs** | Fluid dynamics | Chebyshev marginal-stability eigenproblem | **Ra_c ≈ 816.7, k_c ≈ 2.21** |
| **#61 CTQW search, simplex of cliques** | Quantum computing | Exact 7×7 symmetry reduction + two-stage protocol | **T ≈ 801, P ≈ 0.98** |

Each is self-validating: the SYK closed form gives 0 for q=2 (free fermions) and ½ln2 at large
q; the Rayleigh–Bénard solver reproduces the textbook rigid-rigid (1707.76), free-free (657.5)
and rigid-free (1100.65) numbers to four significant figures before the mixed-BC case; the
quantum-search 7×7 reduction has the same spectrum as Meyer–Wong's published matrix.

## 3 · Six new CritPt-style challenges

Same schema as CritPt (`new_challenges/*.json`: a research setup, one machine-verifiable answer,
a code template, plus a harder checkpoint). All answers verified in
`critpt_repro/repro/verify_new_questions.py`.

| ID | Title | Subfield | Verified answer |
|---|---|---|---|
| NC1 | SYK residual entropy at q=6 | High-energy / CMT | S/N = 0.2908 |
| NC2 | Efimov discrete scaling factor | AMO / few-body | λ = 22.69 |
| NC3 | KCBS contextuality quantum bound | Quantum foundations | √5 = 2.2361 |
| NC4 | Rayleigh–Bénard, fixed-flux walls | Fluid dynamics | Ra_c = 720, k_c → 0 |
| NC5 | Search on joined complete graphs | Quantum computing | T = π√n/2, P = ½ |
| NC6 | One-axis-twisting spin squeezing | AMO / metrology | ξ²_min = 0.063 (−12.0 dB) |

---

## Repository layout

```
EigenValue/
├── docs/
│   ├── subfield_paper_analysis.md       # analysis of the 70 challenges (Chinese)
│   └── subfield_paper_analysis.en.md    # English translation
└── critpt_repro/
    ├── README.md                        # workbench overview
    ├── REPRODUCTIONS.md                 # the 3 reproductions, in detail
    ├── NEW_CRITPT_QUESTIONS.md          # the 6 new challenges, human-readable
    ├── presentation.html                # visual summary (self-contained)
    ├── papers/manifest.csv              # 27 source papers (PDFs git-ignored; re-fetchable)
    ├── challenges/                       # 13 public CritPt challenge JSONs studied
    ├── new_challenges/                   # 6 new challenges in CritPt JSON schema
    └── repro/                            # runnable reproduction + verification scripts
```

The 27 source PDFs (~119 MB) are intentionally **not committed**; `papers/manifest.csv` lists
every arXiv ID so they can be re-downloaded.

## Reproduce

```bash
pip install -r requirements.txt        # numpy, scipy, mpmath

cd critpt_repro/repro
python3 repro_61_quantum_search.py     # T=801, P=0.98                (~15 s)
python3 repro_31_rayleigh_benard.py    # Ra_c=816.7, k_c=2.21 + solver validation
python3 repro_17_syk_entropy.py        # S/N=0.2324 (closed form) + finite-N ED
python3 verify_new_questions.py        # all six new-challenge answers
python3 make_new_challenges.py         # regenerate new_challenges/*.json

# Re-download the source papers (needs internet):
#   arXiv IDs are in critpt_repro/papers/manifest.csv
```

Requires Python 3 with `numpy`, `scipy`, `mpmath` (see [`requirements.txt`](requirements.txt)).

## Roadmap & license

Next steps — an automated grader, a second batch of reproductions, CI, and upstream
contribution — are in [`ROADMAP.md`](ROADMAP.md). Released under the
[MIT License](LICENSE) (covers this repo's own code and documentation; the referenced papers
remain under their publishers' terms and are not redistributed here).

## References

CritPt benchmark: *Probing the Critical Point (CritPt) of AI Reasoning: a Frontier Physics
Research Benchmark*, [arXiv:2509.26574](https://arxiv.org/abs/2509.26574);
dataset/code: [github.com/CritPt-Benchmark/CritPt](https://github.com/CritPt-Benchmark/CritPt).
Per-challenge source papers are cited in the analysis docs and `papers/manifest.csv`.
