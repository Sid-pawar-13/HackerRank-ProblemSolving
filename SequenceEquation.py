import numpy as np

def permutationEquation(p):
    print(p)
    return [p.index(p.index(i+1)+1)+1 for i in range(len(p))]
print(permutationEquation(list(np.random.randint(50,size = np.random.randint(50,size = 1)))))
