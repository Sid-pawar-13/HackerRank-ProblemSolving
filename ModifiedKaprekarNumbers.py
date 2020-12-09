import numpy as np

def kaprekarNumbers(p, q):
    print(p,q)
    f = []
    for i in range(p,q+1):
        if i==1:
            f.append(i)
        elif i>3:
            n=str(i**2)
            l=int(len(n)/2)
            if (int(n[:l])+int(n[l:]))==i:
                f.append(i)
    print(*f) if len(f)!=0 else print('INVALID RANGE')

kaprekarNumbers(int(np.random.randint(1,11,size=1)),int(np.random.randint(1,100,size=1)))
