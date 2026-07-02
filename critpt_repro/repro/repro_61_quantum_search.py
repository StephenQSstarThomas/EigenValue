"""
CritPt Challenge 61 reproduction: CTQW spatial search on a "simplex of complete graphs".
Ref: Meyer & Wong, "Connectivity is a poor indicator of fast quantum search", PRL/arXiv:1409.5876.

Challenge M=200 uses an "(M/2)-simplex" (=M/2+1 cliques) of cliques of M/2 vertices.
=> in Meyer-Wong notation their m == M/2 == 100.  Total vertices N = m(m+1) = 100*101 = 10100.

The whole search dynamics lives in a 7-dim symmetric subspace with basis (a,b,c,d,e,f,g).
Two exact, independent constructions of the 7x7 H are built and cross-checked:
  (A) Meyer-Wong's explicit matrix (their Eq.), and
  (B) an equitable-partition quotient derived from the raw graph (vertices = ordered pairs).
Then the Meyer-Wong two-stage protocol is run and P(|a>) read off.
"""
import numpy as np

m = 100                     # = M/2 (Meyer-Wong's M)
M1, M2 = m-1, m-2
N = m*(m+1)                 # 10100
sizes = np.array([1, M1, 1, M1, M1, M1, M1*M2], float)   # |a|,|b|,...,|g|
assert sizes.sum() == N

# ---------- (A) Meyer-Wong explicit adjacency in symmetric basis (a,b,c,d,e,f,g) ----------
s1, s2 = np.sqrt(M1), np.sqrt(M2)
B = np.array([
 [0,  s1, 1,  0,  0,  0,  0 ],
 [s1, M2, 0,  0,  1,  0,  0 ],
 [1,  0,  0,  s1, 0,  0,  0 ],
 [0,  0,  s1, M2, 0,  1,  0 ],
 [0,  1,  0,  0,  0,  1,  s2],
 [0,  0,  0,  1,  1,  0,  s2],
 [0,  0,  0,  0,  s2, s2, M2],
], float)
assert np.allclose(B, B.T)

# ---------- (B) equitable-partition quotient from the raw graph, as a cross-check ----------
# vertices (i,j), i!=j in {0..m}; a=(0,1). classes ordered to match (a,b,c,d,e,f,g):
# a=(0,1); b=(0,j>=2); c=(1,0); d=(1,j>=2); e=(j>=2,0); f=(j>=2,1); g=(j,k>=2)
bnb = np.zeros((7,7))
bnb[0,1]=M1; bnb[0,2]=1                     # a: b(M1), c(1)
bnb[1,0]=1; bnb[1,1]=M2; bnb[1,4]=1         # b: a,(M-2)blue, green
bnb[2,0]=1; bnb[2,3]=M1                     # c: a, d(M1)
bnb[3,2]=1; bnb[3,3]=M2; bnb[3,5]=1         # d: c,(M-2)magenta, brown
bnb[4,1]=1; bnb[4,5]=1; bnb[4,6]=M2         # e: blue, brown, (M-2)white
bnb[5,3]=1; bnb[5,4]=1; bnb[5,6]=M2         # f: magenta, green, (M-2)white
bnb[6,4]=1; bnb[6,5]=1; bnb[6,6]=M2         # g: green, brown, (M-3)white+1match
sq = np.sqrt(sizes)
B2 = bnb*(sq[:,None]/sq[None,:])
assert np.allclose(B2, B2.T, atol=1e-9)
assert np.allclose(np.sort(np.linalg.eigvalsh(B)), np.sort(np.linalg.eigvalsh(B2)), atol=1e-9), \
    "equitable-partition H disagrees with Meyer-Wong matrix"
print("[check] equitable-partition quotient == Meyer-Wong 7x7 matrix  (spectra match)")

marked = np.zeros((7,7)); marked[0,0] = 1.0     # -|a><a|
def Ham(g): return -g*B - marked
def propagate(psi, g, t):
    w,V = np.linalg.eigh(Ham(g))
    return V @ (np.exp(-1j*w*t) * (V.T @ psi))

psi_s = sq/np.sqrt(N)                            # uniform superposition |s>
ea = np.zeros(7); ea[0]=1                        # <a|
eb = np.zeros(7); eb[1]=1                        # <b|

# ---------- gaps at the two critical gammas (probe with the two states of that stage) ----------
def two_level_gap(g, v0, v1):
    w,V = np.linalg.eigh(Ham(g))
    ov = (np.abs(v0@V)**2)*(np.abs(v1@V)**2)
    i,j = np.argsort(-ov)[:2]
    return abs(w[i]-w[j])
g1, g2 = 2.0/m, 1.0/m
psi_s0 = np.sqrt(sizes)/np.sqrt(N)
eb_v = np.zeros(7); eb_v[1]=1
ea_v = np.zeros(7); ea_v[0]=1
gap1 = two_level_gap(g1, psi_s0, eb_v)   # |s>-|b> stage; expect ~ 4/m^{3/2}
gap2 = two_level_gap(g2, eb_v, ea_v)     # |b>-|a> stage; expect ~ 2/sqrt(m)
print(f"[stage1] gamma_c1=2/m={g1:.5f}  numeric gap={gap1:.6e}  vs 4/m^1.5={4/m**1.5:.6e}")
print(f"[stage2] gamma_c2=1/m={g2:.5f}  numeric gap={gap2:.6e}  vs 2/sqrt(m)={2/np.sqrt(m):.6e}")

# ---------- analytic two-stage times ----------
t1 = np.pi*m**1.5/4       # |s> -> |b>
t2 = np.pi*np.sqrt(m)/2   # |b> -> |a>
T_total = t1 + t2

# run the exact two-stage protocol with analytic times
psi = propagate(psi_s, g1, t1)
P_b_after1 = abs(eb@psi)**2
psi = propagate(psi, g2, t2)
P_a = abs(ea@psi)**2

# also optimize t1,t2 around analytic values to get the true achievable max
def scan_stage(psi_in, g, tc, target_vec, half=0.15, npts=4000):
    ts = np.linspace(tc*(1-half), tc*(1+half), npts)
    w,V = np.linalg.eigh(Ham(g)); c = V.T@psi_in; tv = target_vec@V
    amp = tv[None,:]*c[None,:]*np.exp(-1j*np.outer(ts,w))
    P = np.abs(amp.sum(1))**2
    k = np.argmax(P); return ts[k], P[k]
t1o, _   = scan_stage(psi_s, g1, t1, eb)
psi1 = propagate(psi_s, g1, t1o)
t2o, Pao = scan_stage(psi1, g2, t2, ea)

print("\n=== RESULTS (Challenge 61, M=200 => Meyer-Wong m=100) ===")
print(f"total vertices N            = {N}")
print(f"stage-1 time  t1 = pi m^1.5/4 = {t1:.4f}")
print(f"stage-2 time  t2 = pi sqrt(m)/2 = {t2:.4f}")
print(f"TOTAL TIME    T  = t1+t2      = {T_total:.4f}   -> rounded int = {round(T_total)}")
print(f"P(|b>) after stage 1         = {P_b_after1:.4f}")
print(f"P(|a>) after stage 2 (analytic times) = {P_a:.4f}  -> 2dp = {P_a:.2f}")
print(f"P(|a>) with locally-optimized times   = {Pao:.4f}  (t1={t1o:.2f}, t2={t2o:.2f})")

