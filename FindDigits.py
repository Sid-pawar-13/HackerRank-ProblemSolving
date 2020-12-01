import numpy as np

def findDigits(n):
    print(n)
    return len([x for x in list(str(n)) if int(x)!=0 and n%int(x)==0])
print(findDigits(int(np.random.randint(100000000,size=1))))
