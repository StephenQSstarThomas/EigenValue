# CritPt public challenge set — subfield & related-paper analysis

English translation of `subfield_paper_analysis.md`. This report consolidates the analysis of
70 public CritPt test challenges by four read-only sub-agents. Source files used:

- `repo/data/public_test_challenges/json/Challenge_*.json`
- `source/text/06-SI.tex`
- `source/main.bbl`
- `reference_index.csv`

Important note: `06-SI.tex` gives the *aggregate* reference list for the test set, not a
per-problem binding. The "related papers" column below is therefore a nearest-neighbour match
based on each problem's title, keywords, and the `main.bbl` entries; low-confidence or
method-level-only matches are flagged explicitly.

## Overall structure

These 70 problems are "verifiable small tasks" drawn from frontier physics research — not
traditional textbook problems. High-density directions include:

- **Condensed matter & quantum many-body:** moiré/FCI, FQH/anyons, Hubbard/Hatsugai-Kohmoto,
  Kitaev, PXP scars, topological crystals, quantum geometry.
- **High-energy, gravity, cosmology & QCD:** holographic Weyl anomaly, AdS/BCFT,
  inflation/torsion, SYK, LaMET/quasi-PDF, Schwinger-Keldysh hydrodynamics, CFT correlators.
- **Quantum information, computing & foundations:** distributed sensing, Holevo information,
  tensor networks, inverse Hamiltonian, quantum capacity, contextuality, relative-entropy
  contraction.
- **AMO, optics & precision measurement:** HHG, optical binding, OPA, levitated optomechanics,
  Penning-trap cavity shift, spin squeezing, Yb magic wavelengths, superresolution.
- **Statistical physics, nonlinear, fluids, biophysics & astro detection:** cell-size stochastic
  growth, RBC/Rayleigh-Darcy, autocatalytic cycles, Efimov physics, dark-matter interferometer
  detection.

## Per-problem subfield & most-relevant paper

| # | Title | Subfield | Most-relevant paper candidate | Confidence |
|---:|---|---|---|---|
| 1 | Holographic Weyl anomaly | AdS/CFT; holographic renormalization; Weyl anomaly; obstruction tensor | Jia & Karydas, *Obstruction tensors in Weyl geometry and holographic Weyl anomaly* (2021); Graham, *Extended obstruction tensors...* (2009); Henningson & Skenderis, *The holographic Weyl anomaly* (1998) | High |
| 2 | Population growth rate from stochastic model of growth and cell-size regulation | Cell-size control; stochastic single-cell growth; size-structured population dynamics | Levien et al. (2025); Barber et al. (2021); Jafarpour et al. (2018) | High |
| 3 | Geodesic in AdS/BCFT of a black hole | AdS/BCFT; AdS3/BTZ black hole; brane; geodesic approximation | Fujita, Takayanagi & Tonni, *Aspects of AdS/BCFT* (2011); Grinberg & Maldacena (2021); Geng & Jiang (2025) | Med-high |
| 4 | Orbital angular momentum conservation in high harmonic generation | Strong-field nonlinear optics; HHG; attosecond vortex; spin-orbital-AM conservation | Dorney et al. (2019); Rego et al. (2019); Hernández-García et al. (2013) | High |
| 5 | Marchenko-Pastur entropy | Random matrix theory; entropy of the MP distribution; hypergeometric analytic continuation | Bartolotta et al. (2022); Collins & Śniady (2006) | Low-med, nearest-neighbour |
| 6 | Twisted Bilayer MoTe2 | TMD moiré Chern bands; FCI; band quantum geometry | Jia et al. (2024); Wang et al. (2024); Reddy et al. (2023) | High |
| 7 | Noisy quantum sensing | Distributed quantum sensing; noisy GHZ networks; QFI | Zang et al. (2025); Zang et al. (2024); Zhang & Zhuang (2021) | High |
| 8 | Scalar spectrum in Nieh-Yan gravity | Nieh-Yan/torsion gravity; natural inflation; FRW scalar perturbations | Freese, Frieman & Olinto (1990); Gluscevic & Kamionkowski (2010); Maleknejad (2016) | Low, exact Nieh-Yan source not matched |
| 9 | Nieh-Yan modified gravity with Torsion in FRW space-time | Torsion cosmology; Nieh-Yan modified gravity; inflation e-folds | Freese et al. (1990); Guth (1981); Linde (1983) | Low-med, inflation background hits, Nieh-Yan misses |
| 10 | Axion inflation with Chern-Simons | Axion inflation; gravitational Chern-Simons; parity violation | Gluscevic & Kamionkowski (2010); Maleknejad (2016); Fujita et al. (2022) | Med |
| 11 | Gapped edge of the Moore-Read state | Moore-Read FQH edge; Majorana-boson edge theory; SUSY sine-Gordon RG | Goldschmidt (1986); Milovanović & Read (1996); Moore & Read (1991) | High |
| 12 | Parafermion zero modes tunneling | FQH-SC heterostructures; parafermion zero modes; tunneling/braiding phase | Cao, Kou & Fradkin (2024); Barkeshli, Jian & Qi (2013); Fendley (2012) | Med-high |
| 13 | Verlinde lines in the Moore-Read CFT | Rational CFT; Verlinde lines; Moore-Read topological order | Verlinde (1988); Moore & Read (1991); Di Francesco et al. (2012) | High |
| 14 | High/low-temperature duality in Ising Torus | Random-bond Ising; Nishimori line; Kramers-Wannier duality; torus sectors | Fröhlich et al. (2004, 2007); Dennis et al. (2002); Nishimori (2001) | Med-high |
| 15 | Decohered AKLT model | 1D SPT/AKLT; string order; mixed-state topology; MPS | Huang et al. (2024); Fan et al. (2024); Cirac et al. (2021) | Low-med, original AKLT source not matched |
| 16 | Interacting Chern insulator | Quarter-filled Chern/Mott insulator; topological Mottness | Mai et al. (2023, 2023, 2024) | High |
| 17 | Zero temperature entropy in Sachdev-Ye-Kitaev models | SYK; large-N random Majorana fermions; residual entropy | Fu & Sachdev (2016); Maldacena & Stanford (2016) | High |
| 18 | Optical binding force | Optical binding; levitated nanoparticles; light-induced dipole-dipole interaction | Rieser et al. (2022); Hoang et al. (2016) | Med-high |
| 19 | Cascade optical parametric amplifier | Quantum optics; OPA; squeezing; lossy cascaded amplification | Manceau et al. (2017); Nehra et al. (2022) | Low-med, nearest-neighbour |
| 20 | Torsional levitated optomechanics | Levitated optomechanics; torsional modes; ellipsoidal nanoparticles | Hoang et al. (2016); Rieser et al. (2022) | High |
| 21 | Numerical LaMET matching | Lattice QCD; LaMET; quasi-PDF matching; DGLAP resummation | Su et al. (2023); Ji et al. (2021); Ji (2013) | High |
| 22 | Single particle Holevo Information | Quantum information; single-particle multiple-access channels; Holevo information | Chen et al. (2024); Zhang et al. (2022); Maisriml et al. (2025) | High |
| 23 | One-loop correction of quasi-PDF | Perturbative QCD; quasi-PDF; one-loop matching | Ji (2013); Ji (2014); Izubuchi et al. (2018) | Med-high |
| 24 | LaMET matching in Coulomb gauge | LaMET; Coulomb-gauge quasi-PDF; perturbative QCD | Ji (2013); Ji et al. (2021); Izubuchi et al. (2018) | Med, exact Coulomb-gauge source not matched |
| 25 | Minimum Doppler factor of a relativistic jet | Blazar jets; photopion cascades; high-energy neutrino source constraints | Murase, Oikonomou & Petropoulou (2018); Padovani et al. (2019) | Med-high |
| 26 | Spherical cavity shifts | Penning trap; spherical microwave cavity; electron cavity shifts | Brown, Helmerson & Tan (1986); Brown & Gabrielse (1986); Barton & Fawcett (1988) | High |
| 27 | One-axis twisting model with dissipation | Spin squeezing; one-axis twisting; decoherence; quantum metrology | Kitagawa & Ueda (1993); Wineland et al. (1994); Ma et al. (2011) | Med-high |
| 28 | Optical conductivity of the Hubbard model | Hubbard model; optical conductivity; Fermi-liquid scattering | Mu, Sun & Millis (2022); Rosch & Howell (2005); Mu et al. (2024) | Med-high |
| 29 | Hubbard model in an optical lattice | Ultracold atoms; optical lattices; Hubbard parameters `t,U` | Greiner et al. (2002); Bloch et al. (2012); Gross & Bloch (2017) | High |
| 30 | Orthogonal non-isometric maps | Random orthogonal maps; Haar/Weingarten integration; non-isometric maps | Collins & Śniady (2006) | Med, method-level match |
| 31 | Linear stability analysis of Rayleigh-Benard convection | Rayleigh-Bénard convection; linear stability; mixed boundary conditions | Liu et al. (2024); Busse (1967); Chandrasekhar | High |
| 32 | Rayleigh-Darcy convection with mixed boundary conditions | Porous-media convection; Darcy law; linear stability | Nield & Bejan (2006); Liu & Knobloch (2022); Hewitt (2020) | High |
| 33 | Condensation of three types of particles | Multi-component long-range interaction; condensation/crystallization; constructive algebraic constraints | Chiesa et al. (2006); Holzmann et al. (2016); Drummond et al. (2008) | Low, nearest-neighbour |
| 34 | Quantum tensor networks | Quantum tensor networks; qMPS circuits; NISQ simulation | Zhang et al. (2022); Foss-Feig et al. (2021); Kim (2017) | Med-high |
| 35 | Quantum inverse problem | Inverse Hamiltonian problem; symmetry-to-Hamiltonian; local Pauli basis | Chertkov & Clark (2018); Chertkov et al. (2020); Qi & Ranard (2019) | High |
| 36 | Oscillation amplitude in transient dynamics of autocatalytic cycles | Autocatalytic reaction cycles; stochastic transient oscillations | Hein & Jafarpour (2024); Dauxois et al. (2009); Togashi & Kaneko (2001) | High |
| 37 | Quantum geometry | Band quantum metric; Wilson loop; Wannier obstruction; Z2 topology | Yu et al. (2025); Yu et al. (2024); Roy (2014) | High |
| 38 | Scattering rate of the Hatsugai-Kohmoto model | Hatsugai-Kohmoto model; Kubo response; strong correlation | Ma et al. (2025); Mai et al. (2024); Zhao et al. (2022) | High |
| 39 | Alteration of cavity field coherences due to atom-cavity interaction | Cavity QED; open systems; coherent field decoherence | Bartolotta et al. (2022); Jäger et al. (2022) | Med-high |
| 40 | Hydrodynamic modes in Schwinger-Keldysh | Fracton/multipole hydrodynamics; dipole/quadrupole symmetry; SK EFT | Jain et al. (2023, 2024); Stahl et al. (2023) | High |
| 41 | Energy in many body quantum systems | Electron gas; DMC/QMC finite-size correction; many-body wavefunction corrections | Holzmann et al. (2016); Chiesa et al. (2006); Drummond et al. (2008) | High |
| 42 | Graphene minimal conductivity | Graphene charged-impurity puddles; Dirac transport; minimum conductivity | Shklovskii (2007); Adam et al. (2007) | Med-high, 3D TI part not matched |
| 43 | Disclination charge | Crystalline topological insulator; rotation symmetry; fractional disclination charge | Li et al. (2020); Zhu et al. (2020) | High |
| 44 | Ground state in Kitaev honeycomb model | Kitaev honeycomb spin liquid; finite-size effects; flux sector | Zschocke & Vojta (2015); Kitaev (2006) | High |
| 45 | Goniopolarity in semiconductor | Anisotropic semiconductor thermopower; direction-dependent Seebeck sign | No locally verifiable paper found with goniopolar/Seebeck/thermopower | Low |
| 46 | PXP scar | Rydberg-blockade PXP chain; quantum many-body scars | Turner et al. (2018, 2018) | High |
| 47 | Integrals of motion | Half-wave maps; continuous Haldane-Shastry chain; Lax pair | Gérard & Lenzmann (2018); Lenzmann & Sok (2020); Zhou & Stone (2015) | High |
| 48 | Lattice Gaussian sum | Multidimensional theta/Gaussian sums; reciprocity; replica analytic continuation | Bellman & Lehman (1961); Fradkin (2009); Parker et al. (2017) | Med |
| 49 | Long-range light cone | Long-range spreading/front propagation; long-range percolation; scrambling analogy | Hallatschek & Fisher (2014); Chatterjee & Dey (2016); Zhou et al. (2023) | Med |
| 50 | Many-body NC Partitions | Noncrossing partitions; minimal transposition factorization; enumerative combinatorics | Simion (2000); Stanley (1986); Collins & Śniady (2006) | Med-high |
| 51 | Random walk a3(t) | Lattice random walk; branching/splitting-recombination walk; generating functions | Brunet (2016); Chatterjee & Dey (2016); Stanley (1986) | Low, nearest-neighbour |
| 52 | Efimov effect in three body problem | Efimov trimer; three-body problem; hyperspherical coordinates | Efimov (1993); Castin & Werner (2011); Colussi et al. (2018) | High |
| 53 | Extended obstruction tensors | Conformal/ambient geometry; Fefferman-Graham metric; extended obstruction tensors | Graham (2009); Fefferman & Graham (2012); Jia & Karydas (2021) | High |
| 54 | Magic wavelengths for Yb isotopes | Yb atomic structure; dynamic polarizability; magic wavelengths | Tang et al. (2018); Safronova et al. (2012); Mitroy et al. (2010) | High |
| 55 | INS cross-section for scattering from an oscillator | Inelastic neutron scattering; phonon/harmonic-oscillator cross section | Chen & Kotlarchyk (2007) | Med-high |
| 56 | Dark matter detection with Cosmic Explorer | Scalar-field dark matter; gravitational-wave interferometer; Cosmic Explorer transducer | Hall & Aggarwal (2022); Grote & Stadnik (2019); Vermeulen et al. (2021) | High |
| 57 | LIGO with modified mirrors for ultralight vector dark matter | Ultralight vector/dark-photon DM; B-L force; interferometer mirrors | Morisaki et al. (2021); Pierce, Riles & Zhao (2018); Miller et al. (2021) | Med-high |
| 58 | Magnetic space group identification | Magnetic space groups; neutron peaks; optical symmetry breaking | Donoway et al. (2024); Sunko et al. (2023) | Med |
| 59 | Charge density wave diffraction | CDW diffraction; periodic strain; structure factor | Overhauser (1971); Abbamonte & Fink (2025); Mitrano et al. (2024) | High |
| 60 | Superresolution | Quantum imaging; two incoherent sources; QFI superresolution | Tsang, Nair & Lu (2016) | High |
| 61 | Quantum search time | Continuous-time quantum-walk search; graph connectivity; complete-graph simplex | Meyer & Wong (2015) | High |
| 62 | Quantum games in multi-slit interference | Multi-slit interference; information-theoretic games; quantum advantage | Horvat & Dakić (2021, 2021) | High |
| 63 | Noise robustness in Kochen-Specker and Spekkens contextuality | Contextuality; KCBS; Spekkens noncontextuality; noise robustness | Klyachko et al. (2008); Spekkens (2005); Kunjwal & Spekkens (2015) | High |
| 64 | Conformal correlators | 2D Ising CFT; spin/energy operators; multi-point correlators | Dotsenko & Fateev (1984); Di Francesco et al. (2012) | High |
| 65 | Constructing fermionic matrix operators | Adjoint matrix models; gauge-invariant trace operators; finite-N trace relations | Aharony et al. (2004); Kinney et al. (2007) | Med |
| 66 | Generating function of index | Supersymmetric/Witten index; adjoint gauge theory; operator counting | Kinney et al. (2007); Aharony et al. (2004) | Med |
| 67 | Quantum capacity for quantum channels | Quantum Shannon theory; private states/channels; quantum capacity | Smith & Wu (2025); Horodecki et al. (2009); Hirche et al. (2022) | Med-high |
| 68 | Quantum f-divergence | Quantum f-divergence; noncommutative relative entropy; monotone metrics | Lesniewski & Ruskai (1999); Hiai & Ruskai (2016) | Med-high, title does not directly match f-divergence |
| 69 | Contraction coefficients for quantum relative entropy | Quantum relative entropy; contraction coefficients; amplitude-damping channel | Hiai & Ruskai (2016); Hirche et al. (2022); Lesniewski & Ruskai (1999) | High |
| 70 | Row-Twirling channel on qubit lattice | Haar twirling; local moment operators; lattice quantum channels | Collins & Śniady (2006); Zhou et al. (2025); Hirche et al. (2022) | Low-med, exact row-twirling source not matched |

## Low-confidence problems needing follow-up review

- **Challenge 5:** no local reference titled "Marchenko-Pastur"; candidates are only entropy/RMT
  nearest neighbours.
- **Challenge 8/9:** the prompt is Nieh-Yan/torsion gravity, but `main.bbl` has no direct Nieh or
  Nieh-Yan entry.
- **Challenge 15:** no hit on the original AKLT paper or a direct AKLT/string-order entry.
- **Challenge 19:** no same-title cascaded-OPA reference.
- **Challenge 24:** no exact Coulomb-gauge quasi-PDF entry; only the LaMET/quasi-PDF foundations.
- **Challenge 30:** only Haar/orthogonal-group integration methodology references.
- **Challenge 33:** looks like a constructive many-body problem; no direct source locally.
- **Challenge 45:** no local goniopolar/Seebeck/thermopower entry found.
- **Challenge 51:** no direct entry for a split-recombine random walk.
- **Challenge 57:** the prompt mentions B-L and modified mirrors; locally only vector/dark-photon
  interferometer nearest neighbours.
- **Challenge 65/66:** the exact source for finite-N trace relations / fermionic matrix operators
  is unclear; Aharony/Kinney are the nearest neighbours.
- **Challenge 70:** no title-level source matched for "Row-Twirling channel".

---

*Reproductions and new challenges built on this analysis live in [`../critpt_repro/`](../critpt_repro/).*
