# Roadmap

Where this project is and where it's going. Today it has: an analysis of the 70 public
[CritPt](https://arxiv.org/abs/2509.26574) challenges, **3 reproductions** (SYK #17,
Rayleigh–Bénard #31, quantum-walk search #61), and **6 new verifiable challenges** across 5
subfields. The aim is to grow this into a self-checking library that reproduces a large fraction
of CritPt and contributes a well-designed set of new challenges back.

Status legend: ✅ done · 🚧 in progress · ⬜ planned.

---

## Phase 1 — Correctness & packaging (near-term)

- ✅ Three reproductions, each validated against known limits.
- ✅ Six new challenges in the CritPt JSON schema, every answer verified.
- ⬜ **Automated grading harness** (`grade.py`) mirroring CritPt's machine verification: load a
  challenge JSON, execute the candidate `answer` function, and check it against the reference —
  numeric tolerance for floats/tuples, `sympy.simplify(a-b)==0` for symbolic answers, array
  comparison for vector outputs. Run it over `new_challenges/` in CI.
- ⬜ **Self-bootstrapping papers** (`fetch_papers.py`): download the 27 source PDFs from
  `papers/manifest.csv` so the repo reproduces from a clean clone without manual steps.
- ⬜ **GitHub Actions CI**: run `verify_new_questions.py` and the fast reproductions
  (`repro_61`, `repro_31`, closed-form part of `repro_17`) on every push.
- ⬜ Ship each reproduction as a runnable **Jupyter notebook** (CritPt distributes `.ipynb`), so
  each derivation reads top-to-bottom with figures (R(a) stability curve, S(T)/N entropy curve,
  P(t) search probability).

## Phase 2 — Coverage (mid-term)

- ⬜ **Reproduce a second batch** of high-confidence, computationally tractable challenges
  flagged in the analysis:
  - #5 Marchenko–Pastur entropy (hypergeometric derivative → closed form)
  - #37 quantum geometry / Wilson-loop bound
  - #44 Kitaev honeycomb ground state (flux sector + finite-size gap)
  - #46 PXP quantum many-body scars (ED, |Z₂⟩ revival period & fidelity)
  - #52 Efimov angular wavefunction & normalization
  - #60 two-source superresolution QFI (Tsang formalism)
  - #63 KCBS / Spekkens contextuality noise robustness
  Target: 8–10 reproductions, each self-validated.
- ⬜ **Resolve the low-confidence paper matches** (Challenges 5, 8/9, 15, 19, 24, 30, 33, 45, 51,
  57, 65/66, 70) with targeted literature search; update both analysis docs and `manifest.csv`.
- ⬜ **Deepen the new challenges** with checkpoint decompositions. CritPt averages ~2.7
  checkpoints per challenge (190 across 71); extend each `new_challenges/*.json` toward that
  granularity so partial credit is measurable.
- ⬜ **Broaden subfields** in the new set — currently high-energy/CMT, AMO, foundations, fluids,
  quantum computing, metrology. Add nuclear physics, astrophysics/GW, biophysics, and nonlinear
  dynamics so the new suite spans CritPt's full breadth.

## Phase 3 — Evaluation & contribution (longer-term)

- ⬜ **Difficulty calibration**: run frontier LLMs (with and without code tools) against the six
  new challenges and report accuracy — the whole point of CritPt is that these are hard; measure
  it and tune any question that turns out guessable.
- ⬜ **Contribute upstream**: propose the strongest new challenges to
  [CritPt-Benchmark/CritPt](https://github.com/CritPt-Benchmark/CritPt) with full derivations and
  graders, following their contribution format.
- ⬜ **Reproduction quality report**: a short write-up on how far first-principles reproduction
  can go across CritPt subfields, and where an LLM+tools agent tends to fail (setup ambiguity,
  convention mismatches, large-N vs finite-N, sign/normalization).
- ⬜ **Companion methods library**: promote the reusable pieces — the validated Chebyshev
  marginal-stability solver, the equitable-partition CTQW reducer, the fast generalized-permutation
  SYK builder — into small, documented, importable modules with tests.

---

## Design principles carried forward

- **Guess-resistant answers.** Every challenge must have a specific number / exact expression an
  LLM cannot pattern-match its way to.
- **Independent derivation.** Answers come from the physics, cross-checked against known limits —
  never copied from a benchmark's reference.
- **Self-validation first.** A solver earns trust by reproducing textbook cases (1707.76 / 657.5 /
  1100.65 for stability; q=2→0 for SYK; a published matrix's spectrum for the quantum walk) before
  it's used on a new case.

Contributions and suggestions welcome — see the open ⬜ items above.
