import numpy as np

def taumBday(b, w, bc, wc, z):
    print(b,w,bc,wc,z)
    return (b*z + (b+w)*wc) if (bc > wc + z) else (w*z  + (w + b)*bc) if (wc > bc + z) else (b*bc + w*wc)

print(taumBday(int(np.random.randint(1,11,size=1)),
               int(np.random.randint(1,11,size=1)),
               int(np.random.randint(1,11,size=1)),
               int(np.random.randint(1,11,size=1)),
               int(np.random.randint(1,11,size=1))))
