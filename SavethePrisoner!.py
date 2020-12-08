import numpy as np

def saveThePrisoner(n, m, s):
    if((m-1)%n == 0):
        return s
    return int(s+(m-1)%n if (m-1)%n+s<=n else s+(m-1)%n-n)

print(saveThePrisoner(np.random.randint(100,size=1),
                      np.random.randint(100,size=1),
                      np.random.randint(10,size=1)))
