import numpy as np

def serviceLane(n, cases):
    return [min(width[x:y+1]) for x,y in cases]

print(serviceLane())
