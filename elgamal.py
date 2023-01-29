import random

from params import p
from params import g

def keygen():
    q = (p-1)/2 
    a = random(1,q) 
    sk = a
    pk = pow(g,a) % p
    return pk,sk

def encrypt(pk,m):
    c1 = 0
    c2 = 0
    return [c1,c2]

def decrypt(sk,c):
    m = 0
    return m

