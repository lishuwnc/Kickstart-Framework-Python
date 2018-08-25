from utility import *

def parseGA2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            a, n, p = parseline(fin.readline().rstrip('\n'))
            qin.put((i, a, n, p))
    return t

def solveGA2017(a, n, p):
    res = a % p
    for i in range(2, n + 1):
        res = fastPow(res, i, p)
    return res

def parseGB2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            r = parseline(fin.readline().rstrip('\n'))
            b = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, r, b))
    return t

def solveGB2017(n, r, b):
    e = [[2 ** 31] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            e[i][j] = min(r[i] ^ b[j], r[j] ^ b[i])
            e[j][i] = e[i][j]
    res = 0
    visited = [False] * n
    visited[0] = True
    for i in range(n - 1):
        m = 2 ** 31
        idx = 0
        for j in range(n):
            if visited[j]:
                continue
            if e[0][j] < m:
                idx = j
                m = e[0][j]
        visited[idx] = True
        res += e[0][idx]
        for j in range(n):
            e[0][j] = min(e[0][j], e[idx][j])
    return res

def parseGC2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, m = parseline(fin.readline().rstrip('\n'))
            grid = []
            for j in range(n):
                grid.append(parseline(fin.readline().rstrip('\n')))
            qin.put((i, n, m, grid))
    return t

def solveGC2017(n, m, grid):
    t = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    minimum = [[[[2 ** 31] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            minimum[i][j][0][0] = grid[i][j]
    for k1 in range(n):
        for k2 in range(m):
            for i in range(n - k1):
                for j in range(m - k2):
                    if k1 == 0 and k2 == 0:
                        continue
                    if k1 == 0:
                        minimum[i][j][k1][k2] = min(minimum[i][j][k1][k2 - 1], grid[i][j + k2])
                    elif k2 == 0:
                        minimum[i][j][k1][k2] = min(minimum[i][j][k1 - 1][k2], grid[i + k1][j])
                    else:
                        minimum[i][j][k1][k2] = min(minimum[i][j][k1 - 1][k2], minimum[i][j][k1][k2 - 1], grid[i + k1][j + k2])
    for k1 in range(n):
        for k2 in range(m):
            for i in range(n - k1):
                for j in range(m - k2):
                    for x in range(k1):
                        t[i][j][k1][k2] = max(t[i][j][k1][k2], t[i][j][x][k2] + t[i + x + 1][j][k1 - x - 1][k2])
                    for x in range(k2):
                        t[i][j][k1][k2] = max(t[i][j][k1][k2], t[i][j][k1][x] + t[i][j + x + 1][k1][k2 - x - 1])
                    if k1 > 0 or k2 > 0:
                        t[i][j][k1][k2] += minimum[i][j][k1][k2]
    return t[0][0][n - 1][m - 1]
