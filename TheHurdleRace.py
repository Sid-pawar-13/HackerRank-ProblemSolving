import numpy as np
def hurdleRace(k, height):
    print(k,height,max(height))
    return max(max(height)-k,0)

print(hurdleRace(int(np.random.randint(100,size=1)),np.random.randint(100,size=np.random.randint(100,size=1))))
