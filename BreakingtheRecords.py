import numpy as np
def breakingRecords(scores):
    print(scores)
    min = max = scores[0]
    min_count = max_count = 0
    for i in scores[1:]:
        if i > max:
            max_count += 1
            max = i
        if i < min:
            min_count += 1
            min = i
    return max_count, min_count

print(breakingRecords(np.random.randint(1000,size=np.random.randint(1000,size=1))))
