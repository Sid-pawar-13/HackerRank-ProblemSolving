import numpy as np

def acmTeam(topic):
    lst = []
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            # print(topic[i], topic[j])
            x = int(topic[i]) + int(topic[j])
            # print(x)
            lst.append(len(str(x))-str(x).count("0"))
            # print(lst)
    return [max(lst), lst.count(max(lst))]
