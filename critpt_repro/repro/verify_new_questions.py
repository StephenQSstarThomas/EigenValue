"""
Verify the reference answers for the NEW CritPt-style questions, so every posed question
ships a machine-checked answer.  Each block is grounded in a downloaded paper.
"""
import numpy as np, mpmath as mp
from scipy.optimize import brentq, minimize_scalar
mp.mp.dps = 30
print("="*70)

# --- NQ1/NQ2: SYK residual entropy at q=6 and q=8 (Maldacena-Stanford Eq.2.33) ---
def S0(q):
    D=mp.mpf(1)/q
    return float(mp.mpf('0.5')*mp.log(2)-mp.quad(lambda x:mp.pi*(mp.mpf('0.5')-x)*mp.tan(mp.pi*x),[0,D]))
print(f"NQ1  SYK q=6 : S/N = {S0(6):.4f}")
print(f"NQ2  SYK q=8 : S/N = {S0(8):.4f}")

# --- NQ3: Efimov discrete scaling factor, 3 identical bosons, unitary limit ---
# transcendental eq (attractive hyperradial channel, s=i s0):
#   s0 cosh(pi s0/2) = (8/sqrt3) sinh(pi s0/6)
f = lambda s: s*mp.cosh(mp.pi*s/2) - (8/mp.sqrt(3))*mp.sinh(mp.pi*s/6)
s0 = float(mp.findroot(f, 1.0))
scaling = float(mp.e**(mp.pi/s0))
print(f"NQ3  Efimov s0 = {s0:.6f} ;  discrete scaling factor e^(pi/s0) = {scaling:.4f}")
print(f"       energy ratio between successive trimers = scaling^2 = {scaling**2:.2f}")

# --- NQ4: KCBS contextuality, max quantum value of sum of 5 projectors = sqrt(5) ---
# pentagram unit vectors in R^3 with adjacent orthogonality; max eig of sum Pi_i.
def kcbs_max():
    # Klyachko construction: cos^2(theta) = cos(pi/5)/(1+cos(pi/5))
    c = np.cos(np.pi/5)/(1+np.cos(np.pi/5))
    cth = np.sqrt(c); sth = np.sqrt(1-c)
    V = []
    for i in range(5):
        phi = 4*np.pi*i/5
        V.append([sth*np.cos(phi), sth*np.sin(phi), cth])
    V = np.array(V)
    # check adjacent orthogonality
    orth = max(abs(V[i]@V[(i+1)%5]) for i in range(5))
    S = sum(np.outer(v,v) for v in V)
    return np.linalg.eigvalsh(S).max(), orth
kcbs, orth = kcbs_max()
print(f"NQ4  KCBS: max sum<Pi_i> = {kcbs:.6f}  (sqrt5={np.sqrt(5):.6f}); adj-orth resid={orth:.1e}; classical bound=2")

# --- NQ5, NQ6: Rayleigh-Benard variants (reuse validated solver) ---
import importlib.util
src=open("repro_31_rayleigh_benard.py").read().split("# ---------------- VALIDATION")[0]
ns={}; exec(src, ns)
critical=ns['critical']
# NQ5: rigid-rigid, bottom fixed-T, top fixed-flux (genuinely distinct config)
bc5=dict(top_free=False, bot_free=False, top_flux=True, bot_flux=False)
Rc5,ac5=critical(bc5, N=48, a_bracket=(0.05,3.5))
print(f"NQ5  RBC both no-slip, bottom fixed-T + top fixed-flux: Ra_c={Rc5:.3f}, k_c={ac5:.4f}")
# NQ6: both fixed-flux, rigid-rigid -> classic Ra_c=720, k_c->0
bc6=dict(top_free=False, bot_free=False, top_flux=True, bot_flux=True)
Rc6,ac6=critical(bc6, N=48, a_bracket=(0.02,2.5))
print(f"NQ6  RBC both rigid + both fixed-flux: Ra_c={Rc6:.3f} (classic 720), k_c={ac6:.4f} (->0)")

# --- NQ7: Meyer-Wong "joined complete graphs": two K_{n} joined by one edge ---
# marked vertex away from bridge. Equitable partition (5 classes) -> exact.
# result: success prob -> 1/2, runtime pi*sqrt(n)/2 (n = N/2 = vertices per clique).
def joined_complete(n):
    # classes: a=marked(1), U=other non-bridge in a's clique (n-2), r=bridge vertex a's side(1),
    #          R=bridge vertex other side(1), W=other clique non-bridge (n-2)
    N=2*n
    sizes=np.array([1, n-2, 1, 1, n-2], float)
    # adjacency between classes (complete graph within each side + single bridge edge r-R)
    b=np.zeros((5,5))
    # a: neighbors = all others in its clique = U (n-2) + r (1)
    b[0,1]=n-2; b[0,2]=1
    # U rep: neighbors in clique = a(1)+other U(n-3)+r(1)
    b[1,0]=1; b[1,1]=n-3; b[1,2]=1
    # r (bridge, a-side): neighbors = a(1)+U(n-2)+R(1 bridge)
    b[2,0]=1; b[2,1]=n-2; b[2,3]=1
    # R (bridge other side): neighbors = r(1 bridge)+W(n-2)+ (its own clique's 'a'? no marked)
    #   other clique = complete K_n: R connects to all n-1 others in that clique = W(n-2)+?
    #   other clique has n vertices: R + (n-1) others, all W-type (no marked). so R~ (n-1) W?
    #   but we split W as n-2... let's treat other clique = R(bridge) + (n-1) plain = W has n-1.
    return None  # (superseded below by a cleaner 4-class model)

def joined_complete2(n):
    # cleaner: a-side clique K_n: {a, bridge_a, and n-2 plain_a}; b-side K_n: {bridge_b, n-1 plain_b}
    # classes: a(1), Pa=plain a-side(n-2), Ba=bridge a-side(1), Bb=bridge b-side(1), Pb=plain b-side(n-1)
    sizes=np.array([1, n-2, 1, 1, n-1], float)
    assert sizes.sum()==2*n
    b=np.zeros((5,5))
    b[0,1]=n-2; b[0,2]=1                     # a ~ Pa, Ba
    b[1,0]=1;   b[1,1]=n-3; b[1,2]=1         # Pa ~ a, Pa, Ba
    b[2,0]=1;   b[2,1]=n-2; b[2,3]=1         # Ba ~ a, Pa, Bb(bridge)
    b[3,2]=1;   b[3,4]=n-1                   # Bb ~ Ba(bridge), Pb
    b[4,3]=1;   b[4,4]=n-2                   # Pb ~ Bb, Pb
    # graph is NOT regular: bridge vertices Ba,Bb have degree n, others n-1.
    for r,s in [(0,1),(0,2),(1,2),(2,3),(3,4)]:
        assert abs(sizes[r]*b[r,s]-sizes[s]*b[s,r])<1e-9,(r,s)   # handshake symmetry
    sq=np.sqrt(sizes); Bsym=b*(sq[:,None]/sq[None,:])
    assert np.allclose(Bsym,Bsym.T,atol=1e-9)
    N=2*n; marked=np.zeros((5,5)); marked[0,0]=1
    gc=1.0/n     # optimal gamma ~ 1/n
    # scan gamma near 1/n and time; report max P
    psi_s=sq/np.sqrt(N); ea=np.zeros(5);ea[0]=1
    best=(0,0,0)
    for g in np.linspace(0.6/n,1.6/n,300):
        w,V=np.linalg.eigh(-g*Bsym-marked); c=V.T@psi_s; av=ea@V
        ts=np.linspace(0, np.pi*np.sqrt(n), 6000)
        P=np.abs((av*c)[None,:]*np.exp(-1j*np.outer(ts,w))).sum(1)
        P=np.abs(((av*c)[None,:]*np.exp(-1j*np.outer(ts,w))).sum(1))**2
        k=P.argmax()
        if P[k]>best[2]: best=(g,ts[k],P[k])
    return best
n=256
g,T,P=joined_complete2(n)
print(f"NQ7  joined complete graphs (two K_{n}, N={2*n}): opt gamma={g:.5f}, T={T:.3f}"
      f" (pi*sqrt(n)/2={np.pi*np.sqrt(n)/2:.3f}), P={P:.4f} (->1/2)")

# --- NQ8: Grover / complete-graph search baseline (sanity anchor) ---
def grover(N):
    # H=-gamma A -|a><a|; complete graph, gamma_c=1/N; T=(pi/2)sqrt(N), P->1
    # 2-class equitable partition {a, rest}
    sizes=np.array([1,N-1.]); sq=np.sqrt(sizes)
    b=np.array([[0,N-1],[1,N-2.]]); Bsym=b*(sq[:,None]/sq[None,:])
    marked=np.array([[1.,0],[0,0]]); gc=1.0/N
    psi_s=sq/np.sqrt(N); ea=np.array([1.,0])
    w,V=np.linalg.eigh(-gc*Bsym-marked); c=V.T@psi_s; av=ea@V
    ts=np.linspace(0,np.pi*np.sqrt(N),8000)
    P=np.abs(((av*c)[None,:]*np.exp(-1j*np.outer(ts,w))).sum(1))**2
    k=P.argmax(); return ts[k],P[k]
T,P=grover(1024)
print(f"NQ8  Grover complete graph N=1024: T={T:.3f} ((pi/2)sqrt(N)={np.pi/2*np.sqrt(1024):.3f}), P={P:.4f}")
