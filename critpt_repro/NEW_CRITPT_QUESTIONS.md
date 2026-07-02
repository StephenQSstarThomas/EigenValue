# New CritPt-style challenges

Six research-level physics problems written in the CritPt format (a research `problem setup`
+ a `main problem` with a single **guess-resistant, machine-verifiable** answer + a code
template to fill in). Each is grounded in one of the papers downloaded to `papers/`, and
**every reference answer below was computed and verified in this session**
(`repro/verify_new_questions.py`, `repro/repro_*.py`). Machine-readable versions matching the
CritPt schema are in `new_challenges/*.json` (main problem + a harder checkpoint each).

Design principles borrowed from CritPt: the answer is a specific number / exact expression an
LLM cannot guess; the setup is phrased as a small research task, not a textbook exercise; and
solving it requires actually running the physics (a stability solve, an ED, a transcendental
root, a variational optimum), not recalling a fact.

| # | Title | Subfield | Verified answer |
|---|-------|----------|-----------------|
| NC1 | SYK residual entropy at q=6 | High-energy / condensed matter | **S/N = 0.2908** (q=8: 0.3136) |
| NC2 | Efimov discrete scaling factor | AMO / few-body | **λ = 22.69** (s₀ = 1.00624) |
| NC3 | KCBS contextuality quantum bound | Quantum foundations | **√5 = 2.2361** |
| NC4 | Rayleigh–Bénard onset, fixed-flux walls | Fluid dynamics | **Ra_c = 720, k_c → 0** |
| NC5 | CTQW search on joined complete graphs | Quantum computing | **T = π√n/2, P = 0.50** |
| NC6 | One-axis-twisting spin squeezing | AMO / metrology | **ξ²_min = 0.063 (−12.0 dB)** |

---

### NC1 — SYK residual entropy at q = 6  ·  *high-energy / condensed matter*
**Setup.** Majorana SYK with a **six-body** random interaction
`H = Σ_{i₁<…<i₆} J_{i₁…i₆} χ_{i₁}…χ_{i₆}`, Gaussian couplings with a good large-N scaling.
Zero-temperature entropy density `S₀/N` from `log Z = −βE₀ + S₀ + c/2β + …`.
**Main problem.** Compute `S₀/N` for q = 6 to four decimals.
**Answer.** `S₀/N = 0.2908` (checkpoint q = 8 → `0.3136`), from the exact form
`S₀/N = ½ln2 − ∫₀^{1/q} π(½−x)tan(πx)dx`.
**Grounds / verifies.** Maldacena–Stanford, *Remarks on the SYK model*, arXiv:1604.07818.

### NC2 — Efimov discrete scaling factor  ·  *AMO / few-body*
**Setup.** Three identical bosons, zero-range interaction at unitarity; the attractive
hyperspherical channel gives the Efimov tower. The lowest-channel exponent `s = i s₀` solves
`−s cos(πs/2) + (8/√3) sin(πs/6) = 0`.
**Main problem.** Compute the geometric scaling factor `λ = e^{π/s₀}` (successive trimers obey
`Eₙ/Eₙ₊₁ = λ²`), to four significant figures.
**Answer.** `λ = 22.69` (`s₀ = 1.00624`; energy ratio `λ² ≈ 515`).
**Grounds / verifies.** Efimov (1970); Castin & Werner, arXiv:1103.5157.

### NC3 — KCBS contextuality quantum bound  ·  *quantum foundations*
**Setup.** One qutrit, five pentagram projectors with cyclic exclusivity
`⟨v_i|v_{i+1}⟩ = 0`. Noncontextual models obey `Σ⟨Π_i⟩ ≤ 2`.
**Main problem.** Maximum of `Σ_{i=0}^4 Tr(ρ Π_i)` over all qutrit states.
**Answer.** `√5 = 2.23607` (= largest eigenvalue of `Σ_i Π_i`; classical bound 2).
**Grounds / verifies.** Klyachko, Can, Binicioğlu, Shumovsky, PRL 101, 020403 (arXiv:0706.0126).

### NC4 — Rayleigh–Bénard onset with fixed-flux walls  ·  *fluid dynamics*
**Setup.** Boussinesq convection, both walls **no-slip** and both imposing **fixed heat flux**
(`∂_z θ = 0`). Marginal linear stability.
**Main problem.** Critical Rayleigh number (±1) and horizontal wavenumber.
**Answer.** `Ra_c = 720`, `k_c → 0` (long-wavelength onset — the classic fixed-flux result).
Checkpoint (rigid–rigid, bottom fixed-T / top fixed-flux): `Ra_c ≈ 1295.8, k_c ≈ 2.55`.
**Grounds / verifies.** Chandrasekhar, *Hydrodynamic Stability*; Liu et al., arXiv:2312.06030.
Solved with the same Chebyshev solver validated in Challenge 31 (rigid-rigid 1707.76 etc.).

### NC5 — CTQW search on joined complete graphs  ·  *quantum computing*
**Setup.** Search `H = −γA − |a⟩⟨a|` on two `K_n` (N = 2n) joined by a single bridge edge, the
marked vertex away from the bridge; initial uniform state.
**Main problem.** Optimal runtime `T(n)` and success probability `P`.
**Answer.** `T = π√n/2`, `P = 1/2` (the bridge caps probability transfer at one clique).
Checkpoint (Grover, single `K_N`): `T = (π/2)√N`, `P = 1`.
**Grounds / verifies.** Meyer & Wong, *Connectivity is a poor indicator of fast quantum
search*, arXiv:1409.5876 (same paper as Challenge 61).

### NC6 — One-axis-twisting spin squeezing  ·  *AMO / metrology*
**Setup.** `N` atoms, coherent spin state along `+x`, evolving under `H = χ J_z²`; Wineland
parameter `ξ² = N(ΔJ_⊥,min)²/|⟨J⟩|²`.
**Main problem.** Minimum `ξ²_min` over twisting time for N = 100, to two significant figures.
**Answer.** `ξ²_min = 0.063` (−12.0 dB); checkpoint N = 50 → `0.104`; scales as `N^{−2/3}`
(verified ratios 0.605 ≈ 2^{−2/3}).
**Grounds / verifies.** Kitagawa & Ueda, PRA 47, 5138; Ma, Wang, Sun, Nori review, arXiv:1011.2978.
