def sockMerchant(n, ar):
    count = {}
    for element in ar:
        if element in count:
            count[element] += 1
        else:
            count[element] = 1
    num_count = list(count.values())
    result = []
    for i in num_count:
        i = i//2
        result.append(i)
    return sum(result)
