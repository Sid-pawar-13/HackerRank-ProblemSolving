import numpy as np

def minimumDistances(a):
    print(a)
    min=index=1000
    for i in range(len(a)-1):
        if a[i] in a[i+1:]:
            index=a[i+1:].index(a[i])
            if (index) < min:
                min=(index+1)
    return min if min!=1000 else -1

print(minimumDistances(list(np.random.randint(100,size=np.random.randint(15,size=1)))))
