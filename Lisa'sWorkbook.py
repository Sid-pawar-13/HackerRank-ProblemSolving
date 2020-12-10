import numpy as np

def workbook(n, k, arr):
    page = 0
    sp=0
    for i in range(n):
        page +=1
        for j in range(1,arr[i]+1):
            if j==page:
                sp+=1
            if(j%k==0 and j!=arr[i]):
                page+=1
    return sp

print(workbook(5,3,[4,2,6,1,10]))
