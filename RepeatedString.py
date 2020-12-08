import numpy as np

def repeatedString(s, n):
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")

print(repeatedString('aba',10))
