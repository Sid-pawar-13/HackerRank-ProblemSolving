import numpy as np

def circularArrayRotation(a, k, queries):
    for i in range(k):
        temp = a.pop(len(a)-1)
        a.insert(0,temp)
    return [a[j] for j in queries]

print(circularArrayRotation([3,4,5],2,[1,2]))
