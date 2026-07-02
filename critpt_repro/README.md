# CritPt reproduction & new-question workbench

Work built from `docs/subfield_paper_analysis.md` (the analysis of the 70 public
[CritPt](https://arxiv.org/abs/2509.26574) frontier-physics challenges). CritPt = *Complex
Research using Integrated Thinking – Physics Test*: 71 research-level, machine-verifiable
physics challenges where the best LLM scores ~10%.

## What's here

```
critpt_repro/
├── papers/              27 source papers (arXiv PDFs) + manifest.csv
├── challenges/          13 public CritPt challenge JSONs pulled for study
├── repro/               reproduction + verification scripts (all runnable)
├── new_challenges/      6 NEW CritPt-format challenge JSONs (main + checkpoint)
├── REPRODUCTIONS.md     the 3 end-to-end reproductions, with results
└── NEW_CRITPT_QUESTIONS.md   the 6 new questions, human-readable
```

## 1. Papers downloaded
27 of the papers referenced in the analysis were fetched from arXiv (see
`papers/manifest.csv`) — SYK, Meyer–Wong quantum search, fixed-flux Rayleigh–Bénard, Tsang
superresolution, MoTe₂ FCI, PXP scars, LaMET, Efimov, optical binding, Mottness/HK, KCBS,
inverse Hamiltonian, tensor networks, mixed-state SPT, dipole hydrodynamics, dark-matter
transducers, Kitaev honeycomb, quantum geometry, spin squeezing, and more. (1 of 28 targets,
Dorney et al. HHG, is journal-only with no preprint.)

## 2. Three end-to-end reproductions  →  `REPRODUCTIONS.md`
The public benchmark ships every answer **blanked out**, so each was derived independently:

- **Challenge 17 — SYK zero-T entropy** → `S/N = 0.2324` (Maldacena–Stanford closed form,
  self-validated at q=2→0 and large-q; independent finite-N ED confirms a nonzero residual
  entropy trending to it).
- **Challenge 31 — Rayleigh–Bénard, mixed BCs** → `Ra_c ≈ 816.7, k_c ≈ 2.21` (Chebyshev
  marginal-stability solver, validated to 4 sig figs against the rigid-rigid 1707.76,
  free-free 657.5, rigid-free 1100.65 classics).
- **Challenge 61 — CTQW search, simplex of complete graphs** → `T ≈ 801, P ≈ 0.98` (exact 7×7
  symmetry reduction matching Meyer–Wong's matrix; two-stage protocol).

## 3. Six new CritPt-style questions  →  `NEW_CRITPT_QUESTIONS.md`, `new_challenges/*.json`
Same format and spirit as CritPt (guess-resistant machine-verifiable answers, research-task
framing). Every answer was computed & verified this session (`repro/verify_new_questions.py`):
SYK q=6 (0.2908), Efimov scaling (22.69), KCBS (√5), fixed-flux Rayleigh–Bénard (720),
joined-complete-graph search (π√n/2, ½), one-axis-twisting squeezing (0.063).

## Reproduce
```bash
cd repro
python3 repro_61_quantum_search.py     # ~15 s
python3 repro_31_rayleigh_benard.py    # ~1 s  (prints solver validation)
python3 repro_17_syk_entropy.py        # closed form instant; ED a few min
python3 verify_new_questions.py        # all 6 new-question answers
python3 make_new_challenges.py         # regenerates new_challenges/*.json
```
