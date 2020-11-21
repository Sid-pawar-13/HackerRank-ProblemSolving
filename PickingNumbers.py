import numpy as np
def pickingNumbers(a):
    print(a)
    return max([a.count(i)+a.count(i-1) for i in a])
print(pickingNumbers(list(np.random.randint(10,size=np.random.randint(10,size=1)))))
