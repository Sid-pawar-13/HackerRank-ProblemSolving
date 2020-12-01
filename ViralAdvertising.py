import numpy as np

def viralAdvertising(n):
    print(n)
    ppl = [2]
    for i in range(n-1):
        ppl.append(ppl[-1]*3//2)
    return sum(ppl)

print(viralAdvertising(int(np.random.randint(50,size=1))))
