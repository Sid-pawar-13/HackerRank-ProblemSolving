import numpy as np
def birthday(s, d, m):
    print(s,d,m)
    slen = len(s)
    return sum(1 for i in range(slen-m+1) if sum(s[i:i+m])==d)
print(birthday(np.random.randint(1,5,size=np.random.randint(100,size=1)),
         int(np.random.randint(1,31,size=1)),
         int(np.random.randint(1,12,size=1))))
