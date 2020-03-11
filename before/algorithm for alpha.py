from sympy import *
import math
def getMeRatio(t, T, S, ST, C, K, r, L, sigma, miu):
    v1 = math.sqrt(S**2*math.exp(2*miu*(T-t))*(math.exp(sigma**2*(T-t)))-1)
    v2 = math.sqrt(r)
    v3 = S*math.exp(miu*(T-t))
    v4 = v1/v2+v3
    
    v5 = C*math.exp(r*T)+K

    h = (L-v4)/(v5-v4)
    return h


