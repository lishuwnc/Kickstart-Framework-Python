from utility import *

def parseAAA2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            s = []
            for j in range(n):
                s.append(fin.readline().rstrip('\n'))
            qin.put((i, n, s))
    return t

def solveAAA2017(n, s):
    s.sort(key=lambda x: (-len(set(x) - set(' ')), x))
    return s[0]

def parseAAB2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            r, c = parseline(fin.readline().rstrip('\n'))
            grid = []
            for j in range(r):
                grid.append(parseline(fin.readline().rstrip('\n')))
            qin.put((i, r, c, grid))
    return t

def solveAAB2017(r, c, grid):

