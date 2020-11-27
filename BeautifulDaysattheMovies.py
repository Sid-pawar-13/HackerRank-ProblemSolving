import numpy as np

def beautifulDays(i, j, k):
    print(i,j,k)
    return sum([1 for day in range(i, j+1) if (day - int(str(day)[::-1])) % k == 0])

print(beautifulDays(int(np.random.randint(1000,size=1)),
              int(np.random.randint(1000,size=1)),
              int(np.random.randint(100,size=1))))
