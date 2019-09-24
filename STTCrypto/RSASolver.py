# -*- coding: cp65001 -*-
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Arithmetic import modinv, egcd

def inter(n):
    if type(n) == type("p"):
        return int(n.replace(' ',''))
    else:
        return int(n)

def alpetron(s):
    return s.split('×')

def solve(p,q,c,e):
    p = inter(p)
    q = inter(q)
    n = p*q
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    return long_to_bytes(pow(c,d,n))
    
    
def rabin(p,q,c):
    ct = c
    n = p * q
    mp = pow(ct, (p+1)/4, p)
    mq = pow(ct, (q+1)/4, q)
    g, yp, yq = egcd(p, q)
    r = (yp*p*mq + yq*q*mp) % n
    mr = n - r
    s = (yp*p*mq - yq*q*mp) % n
    ms = n - s
    return [long_to_bytes(num) for num in [r,mr,s,ms]]
