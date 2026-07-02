"""
CritPt Challenge 31 reproduction: linear stability of Rayleigh-Benard convection with MIXED
boundary conditions.  Pr=1, horizontally periodic.
  bottom (z=0): no-slip (rigid) + constant heat flux (fixed-flux, Neumann theta)
  top    (z=1): free-slip (stress-free) + fixed temperature (Dirichlet theta)

Marginal state (principle of exchange of stabilities, growth rate sigma=0). With a = horizontal
wavenumber, R = Rayleigh number, the linearized Boussinesq perturbation eqs reduce to
    (D^2 - a^2)^2 W = a^2 R Theta
    (D^2 - a^2)   Theta = -W
solved as a generalized eigenvalue problem A y = R B y, y=(W,Theta), by Chebyshev collocation
on z in [0,1].  R_c = min over a of the smallest positive eigenvalue; a_c is the minimizer.

Solver is first VALIDATED against three classical fixed-temperature cases with known answers.
Ref: Chandrasekhar, Hydrodynamic and Hydromagnetic Stability; Liu et al., arXiv:2312.06030.
"""
import numpy as np
from numpy.linalg import matrix_power
from scipy.linalg import eig
from scipy.optimize import minimize_scalar

def cheb(N):
    """Trefethen Chebyshev diff matrix + nodes on [-1,1] (x[0]=1 ... x[N]=-1)."""
    if N == 0: return np.array([[0.0]]), np.array([1.0])
    x = np.cos(np.pi*np.arange(N+1)/N)
    c = np.hstack([2., np.ones(N-1), 2.])*(-1)**np.arange(N+1)
    X = np.tile(x,(N+1,1)).T
    dX = X - X.T
    D = (np.outer(c,1./c))/(dX+np.eye(N+1))
    D -= np.diag(D.sum(1))
    return D, x

def solve_Rc(a, N, bc):
    """smallest positive marginal R at wavenumber a, for BC spec bc (dict)."""
    # map [-1,1] -> z in [0,1]:  z=(x+1)/2 ; d/dz = 2 d/dx
    D1x, x = cheb(N)
    D1 = 2*D1x
    D2 = D1@D1
    I  = np.eye(N+1)
    L  = D2 - a*a*I
    L2 = L@L
    n  = N+1
    # unknowns: W (n), Theta (n)
    A = np.zeros((2*n, 2*n)); B = np.zeros((2*n, 2*n))
    # eq1 rows [0:n): L2 W - a^2 R Theta = 0
    A[0:n, 0:n]   = L2
    B[0:n, n:2*n] = a*a*I
    # eq2 rows [n:2n): W + L Theta = 0   (no R)
    A[n:2*n, 0:n]   = I
    A[n:2*n, n:2*n] = L
    # ---- boundary rows: x[0]=1 -> z=1 (top); x[N]=-1 -> z=0 (bottom) ----
    top, bot = 0, N
    def setrow(blockrow_offset, node, vec_W=None, vec_T=None):
        r = blockrow_offset
        A[r,:] = 0.0; B[r,:] = 0.0
        if vec_W is not None: A[r, 0:n]   = vec_W
        if vec_T is not None: A[r, n:2*n] = vec_T
    # W=0 at both walls (impermeable) -> overwrite two eq1 rows
    setrow(top, top, vec_W=I[top]);   # W(top)=0
    setrow(bot, bot, vec_W=I[bot]);   # W(bot)=0
    # velocity condition (2nd) at each wall -> overwrite eq1 rows adjacent
    # use rows 1 and N-1 of eq1 block for the DW/D2W conditions
    rW_top, rW_bot = 1, N-1
    setrow(rW_top, top, vec_W=(D2[top] if bc['top_free'] else D1[top]))  # free:D2W=0, rigid:DW=0
    setrow(rW_bot, bot, vec_W=(D2[bot] if bc['bot_free'] else D1[bot]))
    # temperature condition at each wall -> overwrite two eq2 rows (n+top, n+bot)
    setrow(n+top, top, vec_T=(D1[top] if bc['top_flux'] else I[top]))   # flux:DTheta=0 else Theta=0
    setrow(n+bot, bot, vec_T=(D1[bot] if bc['bot_flux'] else I[bot]))
    w = eig(A, B, right=False)
    w = w[np.isfinite(w)]
    w = w[np.abs(w.imag) < 1e-6*np.maximum(1,np.abs(w.real))].real
    w = w[w > 1e-6]
    return w.min() if w.size else np.inf

def critical(bc, N=48, a_bracket=(0.3, 4.0)):
    f = lambda a: solve_Rc(a, N, bc)
    res = minimize_scalar(f, bracket=None, bounds=a_bracket, method='bounded',
                          options={'xatol':1e-5})
    return res.fun, res.x

# ---------------- VALIDATION against classical fixed-T cases ----------------
print("=== solver validation (fixed-temperature classics) ===")
cases = {
 'rigid-rigid (exp Rc=1707.76, ac=3.117)': dict(top_free=False,bot_free=False,top_flux=False,bot_flux=False),
 'free-free   (exp Rc=657.51, ac=2.221)' : dict(top_free=True, bot_free=True, top_flux=False,bot_flux=False),
 'rigid-free  (exp Rc=1100.65,ac=2.682)' : dict(top_free=True, bot_free=False,top_flux=False,bot_flux=False),
}
for name,bc in cases.items():
    Rc,ac = critical(bc)
    print(f"  {name:42s}: Rc={Rc:9.3f}  ac={ac:.4f}")

# ---------------- CHALLENGE 31: bottom rigid+fixed-flux, top free+fixed-T ----------------
bc31 = dict(top_free=True, bot_free=False, top_flux=False, bot_flux=True)
print("\n=== Challenge 31: bottom no-slip+fixed-flux, top free-slip+fixed-T ===")
for N in (36, 48, 64):
    Rc,ac = critical(bc31, N=N, a_bracket=(0.05,3.5))
    print(f"  N={N:3d}: Ra_c={Rc:.4f}   k_c(a_c)={ac:.4f}")
