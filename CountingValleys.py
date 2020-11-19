import random
import numpy as np
def countingValleys(steps, path):
    print(steps,path)
    alt = valley = 0
    for step in path:
        alt += 1 if step == 'U' else -1
        if(step == 'U' and alt == 0):
            valley += 1
    return valley

mylist = random.choices(["D","U"], k = int(np.random.randint(1,100,size=1)))
print(countingValleys(len(mylist),mylist))
