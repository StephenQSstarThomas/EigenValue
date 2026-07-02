"""Generate NEW CritPt-style challenge JSONs (same schema as the public CritPt set) plus a
human-readable markdown. Every reference answer here was numerically verified in
verify_new_questions.py / repro_*.py during this session."""
import json, os, textwrap

OUT = "/home/shiqiu/EigenValue/critpt_repro/new_challenges"
os.makedirs(OUT, exist_ok=True)

def challenge(cid, tag, setup, main, template, answer_expr, checkpoints=None):
    probs = [{
        "problem_id": f"{cid}_main", "problem_type": "main", "problem_index": None,
        "problem_description": f"\n# Problem setup:\n{setup}\n\n# Main problem:\n{main}\n",
        "code_template": template,
        "answer_code": template.replace("= ...", f"= {answer_expr}   # reference (verified)"),
        "answer_only_code": answer_expr, "testcases": None,
        "metadata": {"settings": {}, "tag": tag, "problem_setup": setup}
    }]
    if checkpoints:
        for i, (pid, desc, tmpl, ans) in enumerate(checkpoints):
            probs.append({
                "problem_id": f"{cid}_{pid}", "problem_type": "checkpoint", "problem_index": i,
                "problem_description": desc, "code_template": tmpl,
                "answer_code": tmpl.replace("= ...", f"= {ans}"), "answer_only_code": ans,
                "testcases": None, "metadata": {"settings": {}, "tag": tag}})
    return {"dataset_name": cid, "source_notebook": f"new_challenges/{cid}.ipynb", "problems": probs}

CH = []

# ---------------- NC1: SYK residual entropy at q=6 (high energy / CMT) ----------------
CH.append(challenge(
 "NewChallenge_1_SYK_q6", "High Energy Physics; Condensed Matter",
 "Consider a Majorana Sachdev-Ye-Kitaev model with a SIX-body random interaction, "
 "$H=\\sum_{i_1<\\dots<i_6} J_{i_1\\dots i_6}\\,\\chi_{i_1}\\cdots\\chi_{i_6}$, with Majorana "
 "fermions $\\{\\chi_a,\\chi_b\\}=\\delta_{ab}$ and Gaussian couplings whose variance scales so "
 "that the model has a good large-$N$ limit ($\\langle J^2\\rangle \\propto J^2/N^5$). Work in "
 "the large-$N$ limit and define the zero-temperature entropy density $S_0/N$ via the "
 "low-temperature expansion $\\log Z=-\\beta E_0+S_0+\\tfrac{c}{2\\beta}+\\cdots$.",
 "Calculate the numerical value of $S_0/N$ for $q=6$ to four decimal places.",
 "import mpmath as mp\n\ndef answer():\n    r\"\"\"Return S0/N for the q=6 Majorana SYK model (float, 4 dp).\"\"\"\n    # ------------------ FILL IN YOUR RESULTS BELOW ------------------\n    S_per_N = ...\n    # ---------------------------------------------------------------\n    return S_per_N\n",
 "0.2908",
 checkpoints=[("q8",
   "\n# Checkpoint: repeat for an EIGHT-body interaction ($q=8$).\n",
   "def answer_q8():\n    S_per_N = ...\n    return S_per_N\n", "0.3136")]))

# ---------------- NC2: Efimov discrete scaling factor (AMO / few-body) ----------------
CH.append(challenge(
 "NewChallenge_2_Efimov_scaling", "Atomic, Molecular & Optical Physics",
 "Three identical bosons interact via a zero-range (contact) potential tuned to the unitary "
 "limit (infinite two-body $s$-wave scattering length, $a\\to\\infty$). In hyperspherical "
 "coordinates the attractive channel produces the Efimov effect: an infinite geometric tower of "
 "three-body bound states. The hyperangular eigenvalue for the lowest channel is $s^2=-s_0^2$ "
 "with $s_0$ real, determined by the transcendental equation "
 "$-s\\cos(\\pi s/2)+\\tfrac{8}{\\sqrt3}\\sin(\\pi s/6)=0$ evaluated on the imaginary axis $s=is_0$.",
 "Compute the discrete (geometric) scaling factor $\\lambda=e^{\\pi/s_0}$ relating consecutive "
 "Efimov trimers (so that successive binding energies satisfy $E_n/E_{n+1}=\\lambda^2$). Report "
 "$\\lambda$ to four significant figures.",
 "import mpmath as mp\n\ndef answer():\n    r\"\"\"Return the Efimov discrete scaling factor lambda = exp(pi/s0) (float).\"\"\"\n    # ------------------ FILL IN YOUR RESULTS BELOW ------------------\n    scaling = ...\n    # ---------------------------------------------------------------\n    return scaling\n",
 "22.6944",
 checkpoints=[("s0",
   "\n# Checkpoint: report s0 itself (the imaginary hyperangular exponent) to 5 dp.\n",
   "def answer_s0():\n    s0 = ...\n    return s0\n", "1.00624")]))

# ---------------- NC3: KCBS contextuality quantum bound (foundations) ----------------
CH.append(challenge(
 "NewChallenge_3_KCBS_bound", "Quantum Information, Science & Technology",
 "The Klyachko-Can-Binicioglu-Shumovsky (KCBS) scenario uses a single spin-1 (qutrit) system "
 "and five rank-1 yes/no measurements $\\{\\Pi_i=|v_i\\rangle\\langle v_i|\\}_{i=0}^{4}$ arranged "
 "on a pentagram, where cyclically adjacent measurements are exclusive, "
 "$\\langle v_i|v_{i+1}\\rangle=0$ (indices mod 5). A noncontextual hidden-variable model obeys "
 "$\\sum_{i=0}^{4}\\langle\\Pi_i\\rangle\\le 2$.",
 "Over all qutrit quantum states $\\rho$, what is the maximum value of "
 "$\\sum_{i=0}^{4}\\mathrm{Tr}(\\rho\\,\\Pi_i)$? Give the exact value.",
 "def answer():\n    r\"\"\"Return the maximum quantum value of the KCBS sum (float).\"\"\"\n    # ------------------ FILL IN YOUR RESULTS BELOW ------------------\n    kcbs_max = ...\n    # ---------------------------------------------------------------\n    return kcbs_max\n",
 "5**0.5   # = 2.2360679..."))

# ---------------- NC4: Rayleigh-Benard critical Rayleigh (fixed-flux) (fluids) ----------------
CH.append(challenge(
 "NewChallenge_4_RayleighBenard_fixedflux", "Fluid Dynamics",
 "Rayleigh-Benard convection between two horizontal plates, Boussinesq, horizontally periodic. "
 "BOTH walls are no-slip (rigid) and BOTH impose a fixed heat flux (Neumann condition on the "
 "temperature perturbation, $\\partial_z\\theta=0$ at each wall). Consider the onset of "
 "convection (marginal linear stability, exchange of stabilities).",
 "Find the critical Rayleigh number (to $\\pm1$) and the associated critical horizontal "
 "wavenumber above which the conduction state is linearly unstable.",
 "def answer():\n    r\"\"\"Return (Ra_c, k_c) for rigid-rigid, fixed-flux/fixed-flux RBC.\"\"\"\n    # ------------------ FILL IN YOUR RESULTS BELOW ------------------\n    Ra_c = ...\n    k_c  = ...\n    # ---------------------------------------------------------------\n    return Ra_c, k_c\n",
 "(720.0, 0.0)",
 checkpoints=[("mixed_thermal",
   "\n# Checkpoint: BOTH walls no-slip, but bottom fixed-temperature and top fixed-flux. "
   "Find (Ra_c, k_c).\n",
   "def answer_mixed():\n    Ra_c, k_c = ...\n    return Ra_c, k_c\n", "(1295.78, 2.552)")]))

# ---------------- NC5: CTQW search comparison (quantum computing) ----------------
CH.append(challenge(
 "NewChallenge_5_JoinedCompleteGraphs_search", "Quantum Information, Science & Technology",
 "Continuous-time quantum-walk spatial search with $H=-\\gamma A-|a\\rangle\\langle a|$ on the "
 "'joined complete graphs': two complete graphs $K_n$ (so $N=2n$ vertices total) connected by a "
 "SINGLE bridge edge between one vertex of each clique. The marked vertex $|a\\rangle$ lies in "
 "one clique, NOT at the bridge. The initial state is the uniform superposition $|s\\rangle$.",
 "In the large-$N$ limit, with $\\gamma$ tuned optimally, give the leading-order optimal "
 "evolution time $T$ (as a formula in $n$) and the success probability $P$ at the marked vertex.",
 "def answer():\n    r\"\"\"Return (T_formula_str, P) for optimal joined-complete-graphs search.\"\"\"\n    # ------------------ FILL IN YOUR RESULTS BELOW ------------------\n    T = ...   # e.g. 'pi*sqrt(n)/2'\n    P = ...\n    # ---------------------------------------------------------------\n    return T, P\n",
 "('pi*sqrt(n)/2', 0.5)",
 checkpoints=[("grover_anchor",
   "\n# Checkpoint (anchor): the SAME search on a single complete graph $K_N$ (Grover's problem). "
   "Give optimal T (formula in N) and success probability P.\n",
   "def answer_grover():\n    T, P = ...\n    return T, P\n", "('(pi/2)*sqrt(N)', 1.0)")]))

# ---------------- NC6: one-axis-twisting optimal spin squeezing (AMO metrology) ----------------
CH.append(challenge(
 "NewChallenge_6_OneAxisTwisting_squeezing", "Atomic, Molecular & Optical Physics",
 "An ensemble of $N$ two-level atoms (collective spin $J=N/2$) is prepared in a coherent spin "
 "state polarized along $+x$ and evolves under the one-axis-twisting (OAT) Hamiltonian "
 "$H=\\chi J_z^2$. Spin squeezing is quantified by the Wineland parameter "
 "$\\xi^2=N\\,(\\Delta J_{\\perp,\\min})^2/|\\langle\\vec J\\rangle|^2$, where the minimum is "
 "over directions perpendicular to the mean spin; $\\xi^2<1$ signals metrologically useful "
 "squeezing beating the standard quantum limit.",
 "For $N=100$ atoms, compute the minimum achievable Wineland squeezing parameter "
 "$\\xi^2_{\\min}$ over the twisting time, to two significant figures.",
 "import numpy as np\n\ndef answer():\n    r\"\"\"Return xi^2_min for N=100 one-axis-twisting (float).\"\"\"\n    # ------------------ FILL IN YOUR RESULTS BELOW ------------------\n    xi2_min = ...\n    # ---------------------------------------------------------------\n    return xi2_min\n",
 "0.063   # = -12.0 dB ; scales as N^(-2/3)",
 checkpoints=[("N50",
   "\n# Checkpoint: repeat for N=50 atoms.\n",
   "def answer_N50():\n    xi2_min = ...\n    return xi2_min\n", "0.104")]))

# placeholders filled at runtime for Kitaev / OAT
KITAEV = os.environ.get("KITAEV_ESITE")
OAT = os.environ.get("OAT_XI2")

for c in CH:
    json.dump(c, open(f"{OUT}/{c['dataset_name']}.json","w"), indent=2, ensure_ascii=False)

print(f"wrote {len(CH)} challenge JSONs to {OUT}")
for c in CH:
    print("  -", c["dataset_name"], "| main +", len(c["problems"])-1, "checkpoint(s)")
