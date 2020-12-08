import numpy as np

def equalizeArray(arr):
    print(arr)
    return len(arr)-max([arr.count(i) for i in arr])

print(equalizeArray(list(np.random.randint(10,size=np.random.randint(10,size=1)))))
