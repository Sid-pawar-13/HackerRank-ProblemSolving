import numpy as np
def bonAppetit(bill, k, b):
    print(bill,k,b)
    print(b - (sum(bill) - bill[k]) // 2 or 'Bon Appetit')

bill = np.random.randint(100,size=np.random.randint(100,size=1))
n = len(bill)
bonAppetit(bill,int(np.random.randint(n,size=1)),sum(bill)/2)
