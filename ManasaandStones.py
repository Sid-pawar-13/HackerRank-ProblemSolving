def stones(n, a, b):
    if a!=b:
        l=[0]*n
        left = 1
        right = n-2
        while left <= right:
            l[left] = right * a + left *b
            l[right] = left * a + right *b
            left+=1
            right-=1
        l[0] = a*(n-1)
        l[n-1] = b*(n-1)
        return sorted(l)
    return [a*(n-1)]
