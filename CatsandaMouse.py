import numpy as np
def catAndMouse(x, y, z):
    a = abs(x - z)
    b = abs(y - z)
    return "Cat A" if a<b else "Cat B" if b<a else "Mouse C"
numlist = np.random.randint(100,size=3)
print(catAndMouse(numlist[0],numlist[1],numlist[2]))
