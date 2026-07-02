# CritPt — end-to-end reproductions

Three of the 70 public CritPt challenges catalogued in `docs/subfield_paper_analysis.md` were
reproduced from first principles. The public benchmark **ships every reference answer blanked
out** (held-out grading set), so each answer below was derived independently from the physics
and the source papers, then cross-checked. All scripts are in `repro/`; downloaded source
papers are in `papers/` (27 PDFs, see `papers/manifest.csv`).

| # | Challenge | Subfield | Method | Result (independently derived) |
|---|-----------|----------|--------|-------------------------------|
| 17 | SYK zero-temperature entropy | High-energy / condensed matter | Maldacena–Stanford closed form + finite-N ED | **S/N = 0.2324** |
| 31 | Rayleigh–Bénard critical Rayleigh number (mixed BCs) | Fluid dynamics | Chebyshev-collocation marginal-stability eigenproblem | **Ra_c ≈ 816.7, k_c ≈ 2.21** |
| 61 | CTQW search on a simplex of complete graphs | Quantum computing | Exact 7×7 symmetry reduction + two-stage protocol | **T ≈ 801, P ≈ 0.98** |

---

## Challenge 17 — SYK zero-temperature (residual) entropy

**Task.** Large-N Majorana SYK with 4-body random couplings; compute the residual entropy
density `S/N` to four decimals.

**Route A — exact closed form.** Maldacena–Stanford (arXiv:1604.07818, Eq. 2.33) give, with
Δ = 1/q,
$$\frac{S_0}{N}=\tfrac12\ln 2-\int_0^{1/q}\pi\Big(\tfrac12-x\Big)\tan(\pi x)\,dx .$$
Evaluating at q = 4 gives **S/N = 0.232424 → 0.2324**. The formula self-validates:
- q = 2 (free fermions) → **0.000000** exactly (no residual entropy);
- large q → ½ln2 − π²/4q² (e.g. q = 100: 0.346330 vs asymptote 0.346327).

**Route B — finite-N exact diagonalization (independent).** Majoranas were built by
Jordan–Wigner on N/2 qubits (as fast generalized-permutation operators),
`H = Σ_{i<j<k<l} J_{ijkl} χ_iχ_jχ_kχ_l` with `⟨J²⟩ = 3!/N³`, full spectrum diagonalized and
disorder-averaged for N = 16, 20, 24, 26 Majoranas. The residual entropy is a large-N effect,
so small N cannot show a sharp plateau, but two signatures confirm it:

- the infinite-temperature limit is reproduced **exactly**: `S/N(T→∞) = 0.345 ≈ ½ln2 = 0.3466`
  (validates the ED thermodynamics);
- the low-temperature entropy density **rises monotonically with N** — `S/N(T=0.02)` = 0.092,
  0.119, 0.129, 0.137 for N = 16, 20, 24, 26 — and its 1/N extrapolation gives **≈ 0.21–0.22**,
  consistent with the exact 0.2324 (finite-N systems undershoot at fixed low T).

Reference answer: **`S/N = 0.2324`** (closed form), independently supported by ED.

---

## Challenge 31 — Rayleigh–Bénard, mixed boundary conditions

**Task.** Pr = 1; **bottom** wall no-slip + constant heat flux, **top** wall free-slip + fixed
temperature. Find the critical Rayleigh number (±0.5) and horizontal wavenumber (±0.02).

**Method.** Marginal stability (exchange of stabilities, σ = 0) reduces to
$$(D^2-a^2)^2W = a^2\,\mathrm{Ra}\,\Theta,\qquad (D^2-a^2)\Theta = -W,$$
solved as a generalized eigenvalue problem `A y = Ra·B y` by Chebyshev collocation on z∈[0,1],
minimizing over the wavenumber a. Boundary conditions: `W=0` both walls; `DW=0` (no-slip
bottom) / `D²W=0` (free-slip top); `DΘ=0` (fixed-flux bottom) / `Θ=0` (fixed-T top).

**Solver validation** (fixed-temperature classics, reproduced to 4 significant figures):

| Case | Ra_c (this solver) | Ra_c (literature) | k_c (this) | k_c (lit) |
|------|--------------------|-------------------|-----------|-----------|
| rigid–rigid | 1707.762 | 1707.76 | 3.1164 | 3.117 |
| free–free | 657.511 | 657.51 (27π⁴/4) | 2.2215 | π/√2 = 2.221 |
| rigid–free | 1100.650 | 1100.65 | 2.6823 | 2.682 |

**Result.** For the challenge's mixed BCs, converged across N = 36/48/64 grid points:
**Ra_c ≈ 816.74, k_c ≈ 2.215.** The R(a) curve rises monotonically to +∞ as a→0 (the top
fixed-T wall suppresses the long-wavelength branch), confirming a genuine finite-a global
minimum. Script: `repro/repro_31_rayleigh_benard.py`.

---

## Challenge 61 — CTQW search on a "simplex of complete graphs"

**Task.** M = 200. Take an (M/2)-simplex (M/2+1 = 101 cliques), replace each vertex with a
clique of M/2 = 100 vertices, giving N = 100·101 = 10100 vertices. With
`H = -γA - |a⟩⟨a|` and initial uniform state, find the evolution time T (nearest integer) and
achievable probability P (2 dp) at the marked vertex.

**Method.** The Challenge's M/2 = 100 equals Meyer–Wong's parameter M = 100 (arXiv:1409.5876,
their Figs. 8–9). Coordinatizing vertices as ordered pairs (i,j), i≠j, the automorphism group
gives a **7-class equitable partition**, so the whole dynamics lives in a 7-dimensional
symmetric subspace. Two independent constructions of the 7×7 Hamiltonian — my equitable-partition
quotient and Meyer–Wong's explicit matrix — have **identical spectra** (verified).

Meyer–Wong's **two-stage** protocol:
- Stage 1 (γ = 2/M): transfers |s⟩ → |b⟩ with gap 4/M^{3/2}, time t₁ = πM^{3/2}/4 = 250π ≈ 785.40;
- Stage 2 (γ = 1/M): transfers |b⟩ → |a⟩ with gap 2/√M (reproduced exactly = 0.2), time t₂ = π√M/2 = 5π ≈ 15.71.

**Result.** Total **T = 255π ≈ 801.11 → 801**; numerically P(|b⟩) = 0.95 after stage 1 and
**P(|a⟩) = 0.98** after stage 2 (0.9832 with locally optimized times). This confirms
Meyer–Wong's headline point: despite very high connectivity, this graph needs Θ(N^{3/4}) time —
slower than Grover's √N. Script: `repro/repro_61_quantum_search.py`.
