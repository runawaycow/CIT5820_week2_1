import random

from params import p
from params import g
#g = 9698439374675276823390863679085787099821687964590973421364530706908301367232976242960049544758496470828675688981570819335336142993170304256564916507021997
#p=17485407687035251201370420829093858071027518631263552549047038216080132036645437679594890870680904087373138192057582526597149370808367592630377967178132719

def keygen():
    q = (p-1)/2 
    a = random.randrange(1,q) 
    #print(a)
    sk = a
    pk = pow(g,a,p) 
    return pk,sk

def encrypt(pk,m):
    r = random.randrange(1,p) 
    c1 = pow(g,r,p) 
    c2 = pow(pk,r,p) * m % p
    return [c1,c2]

def decrypt(sk,c):
    #print(c[1])
    #print(c[0])
    #print(sk)
    m = (pow(c[0],-sk,p)*c[1]) % p
    return m

