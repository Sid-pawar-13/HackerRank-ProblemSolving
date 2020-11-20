import numpy as np
def divisibleSumPairs(n, k, ar):
    print(n,k,ar)
    return sum([1 for i in range(n-1) for j in range(i+1,n) if((ar[i]+ar[j])%k==0)])
ar = np.random.randint(10,size=np.random.randint(2,15,size=1))
print(divisibleSumPairs(len(ar),int(np.random.randint(10,size=1)),ar))
