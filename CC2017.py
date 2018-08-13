from utility import *
import numpy as np

def parseCCA2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            r, c, rs, cs, s = parseline(fin.readline().rstrip('\n'))
            p, q = parseline(fin.readline().rstrip('\n'), dtype_fn=float)
            grid = []
            for j in range(r):
                grid.append(parseline(fin.readline().rstrip('\n'), dtype_fn=str))
            qin.put((i, r, c, rs, cs, s, p, q, grid))
    return t

def solveCCA2017(r, c, rs, cs, s, p, q, grid):
    res = 0
    delta = [-1, 0, 1, 0, -1]
    def helper(x, y, s, d, res):
        if s == 0:
            t = 0
            for x, y in d:
                if grid[x][y] == 'A':
                    _p = p
                else:
                    _p = q
                t += 1 - (1 - _p) ** d[(x, y)]
            res = max(res, t)
        else:
            for i in range(4):
                dx, dy = delta[i], delta[i + 1]
                if 0 <= x + dx < r and 0 <= y + dy < c:
                    d[(x + dx, y + dy)] += 1
                    res = max(res, helper(x + dx, y + dy, s - 1, d, res))
                    d[(x + dx, y + dy)] -= 1
                    if d[(x + dx, y + dy)] == 0:
                        del d[(x + dx, y + dy)]
        return res
    res = helper(rs, cs, s, defaultdict(int), res)
    return res

def parseCCB2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            r, c, k = parseline(fin.readline().rstrip('\n'))
            m = []
            for j in range(k):
                m.append(parseline(fin.readline().rstrip('\n')))
            qin.put((i, r, c, k, m))
    return t

def solveCCB2017(r, c, k, m):
    grid = np.ones((r, c), dtype=np.int64)
    for i in range(k):
        x, y = m[i]
        grid[x, y] = False
    res = 0
    s = min(r, c)
    while True:
        t = np.sum(grid)
        res += t
        if t == 0 or s == 1:
            break
        grid = grid[:-1, :-1] & grid[:-1, 1:] & grid[1:, :-1] & grid[1:, 1:]
        s -= 1
    return res