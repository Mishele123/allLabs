
from math import pow, sin, log10


def check(a):
    if not a:
        print("Not")
    else:
        print("Yes")
        

def access2(xmm0, edx, xmm2, xmm3): 
    xmm7 = pow(xmm0, float(edx))
    xmm6 = sin(xmm2);
    xmm6 = log10(xmm3) + xmm6;

    return check(xmm6 > xmm7);

access2(1.0, 1, 0.5, 100.0)