import numpy as np
import math
def squares(a, b):
    print(a,b)
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)))+1
print(squares(int(np.random.randint(100,size=1)),int(np.random.randint(1000,size=1))))
