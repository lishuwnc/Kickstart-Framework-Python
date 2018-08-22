from utility import *

def parseBA2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            K = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, K))
    return t

def solveBA2017(n, K):
    K.sort()
    res = 0
    m = 10 ** 9 + 7
    for i in range(n):
        res = (res - K[i] * (fastPow(2, n - 1 - i, m) - 1) + K[i] * (fastPow(2, i, m) - 1)) % m
    return res

def parseBB2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            p = []
            p.append(parseline(fin.readline().rstrip('\n'), dtype_fn=float))
            qin.put((i, n, p))
    return t

def solveBB2017(n, p):
    x0, y0 = 0, 0
