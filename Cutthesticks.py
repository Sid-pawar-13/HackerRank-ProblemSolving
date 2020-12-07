import numpy as np

def cutTheSticks(arr):
    print(arr)
    ls = []
    while arr:
        ls.append(len(arr))
        arr = [x for x in arr if x != min(arr)]
    return ls

print(cutTheSticks(list(np.random.randint(10,size = np.random.randint(10,size=1)))))
