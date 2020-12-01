import numpy as np

def migratoryBirds(arr):
    print(arr)
    birds = {1:0,2:0,3:0,4:0,5:0}
    for i in arr:
        birds[i] += 1
    print(birds)
    return max(birds, key=birds.get)
print(migratoryBirds(np.random.randint(1,6,size = np.random.randint(5,100,size=1))))
