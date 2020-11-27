import numpy as np

def angryProfessor(k, a):
    print(k,a)
    return 'YES' if sum(map(lambda x: x <= 0, a)) < k else 'NO'

print(angryProfessor(int(np.random.randint(10,size = 1)),
                     np.random.randint(-10,10,size = np.random.randint(10,size = 1))))
