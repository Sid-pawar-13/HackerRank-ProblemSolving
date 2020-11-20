import numpy as np
def pageCount(n, p):
    print(n,p)
    return min(p//2,n//2-(p//2))
n = int(np.random.randint(100,size=1))
print(pageCount(n,int(np.random.randint(n,size=1))))
