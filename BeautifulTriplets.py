import numpy as np

def beautifulTriplets(d, arr):
    print(d,arr)
    return len([1 for i in range(len(arr)) if arr[i]+d in arr and arr[i]+2*d in arr])

print(beautifulTriplets(3,[1,2,4,5,7,8,10]))
