import numpy as np

def chocolateFeast(n, c, m):
    print(n,c,m)
    totalChoc = noWrap = n//c
    while(noWrap >= m):
        noWrap -= m
        totalChoc += 1
        noWrap += 1
    return totalChoc

print(chocolateFeast(int(np.random.randint(1,100,size=1)),
                     int(np.random.randint(1,10,size=1)),
                     int(np.random.randint(1,10,size=1))))
