from Arithmetic import *

def solveMulti(n,psi,c,e):
    # psi is a list
    ts = []
    xs = []
    ds = []

    for i in range(len(psi)):
            ds.append(modinv(e, psi[i]-1))

    m = psi[0]

    for i in range(1, len(psi)):
            ts.append(modinv(m, psi[i]))
            m = m * psi[i]

    for i in range(len(psi)):
            xs.append(pow((c%psi[i]), ds[i], psi[i]))

    x = xs[0]
    m = psi[0]

    for i in range(1, len(psi)):
            x = x + m * ((xs[i] - x % psi[i]) * (ts[i-1] % psi[i]))
            m = m * psi[i]


    return hex(x%n)[2:-1].decode("hex")
