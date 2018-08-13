from utility import *

def parseDDA2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, m = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, m))
    return t

def solveDDA2017(n, m):
    return 1 - 2 * m / (n + m)

