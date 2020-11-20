import numpy as np
def getMoneySpent(keyboards, drives, b):
    print(keyboards,drives,b)
    return max([sum([x,y]) for x in keyboards for y in drives if sum([x,y]) <= b]+[-1])
print(getMoneySpent(np.random.randint(100,size=np.random.randint(10,size=1)),
                    np.random.randint(100,size=np.random.randint(10,size=1)),
                    int(np.random.randint(100,size=1))))
