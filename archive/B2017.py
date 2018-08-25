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
            for j in range(n):
                p.append(parseline(fin.readline().rstrip('\n'), dtype_fn=float))
            qin.put((i, n, p))
    return t

def solveBB2017(n, p):
    def dis(x, y):
        d = 0
        for _x, _y, w in p:
            d += w * max(abs(x - _x), abs(y - _y))
        return d
    xlo, xhi = -1000, 1000
    d1 = 0
    while xhi - xlo > 1e-8:
        xmid = (xlo + xhi) / 2
        xtmp = (xmid + xhi) / 2
        ylo, yhi = -1000, 1000
        while yhi - ylo > 1e-8:
            ymid = (ylo + yhi) / 2
            ytmp = (ymid + yhi) / 2
            if dis(xmid, ymid) < dis(xmid, ytmp):
                yhi = ytmp
            else:
                ylo = ymid
        d1 = dis(xmid, (ylo + yhi) / 2)
        ylo, yhi = -1000, 1000
        while yhi - ylo > 1e-8:
            ymid = (ylo + yhi) / 2
            ytmp = (ymid + yhi) / 2
            if dis(xtmp, ymid) < dis(xtmp, ytmp):
                yhi = ytmp
            else:
                ylo = ymid
        d2 = dis(xtmp, (ylo + yhi) / 2)
        if d1 < d2:
            xhi = xtmp
        else:
            xlo = xmid
    return d1


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