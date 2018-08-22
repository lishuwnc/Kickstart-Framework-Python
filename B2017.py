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

def parseBC2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, m, k = parseline(fin.readline().rstrip('\n'))
            grid = []
            for j in range(n):
                grid.append(list(fin.readline().rstrip('\n')))
            qin.put((i, n, m, k, grid))
    return t

def solveBC2017(n, m, k, grid):
    res = [[[0] * (k + 1) for j in range(m)] for i in range(n + 1)]
    for i in range(1, k + 1):
        for x in range(n):
            for y in range(m):
                if grid[x][y] == '.':
                    continue
                t = 0
                while True:
                    for r in range(y - t, y + t + 1):
                        res[x][y][i] = max(res[x][y][i], (t + 1) ** 2 + res[x + t + 1][r][i - 1])
                    t += 1
                    if y - t < 0 or y + t >= m or x + t + 1 > n or any([grid[x + t][r] == '.' for r in range(y - t, y + t + 1)]):
                        break
    ret = 0
    for i in range(n):
        for j in range(m):
            ret = max(ret, res[i][j][k])
    return ret