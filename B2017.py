from utility import *

def parseBA(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            K = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, K))
    return t

def solveBA(n, K):
    K.sort()
    res = 0
    for i in range(n):
        res = (res - K[i] * (fastPow(2, n - 1 - i) - 1) + K[i] * (fastPow(2, i) - 1)) % (10 ** 9 + 7)
    return res
