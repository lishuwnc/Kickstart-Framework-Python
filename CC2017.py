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

def parseCCC2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            expr = []
            for j in range(n):
                expr.append(fin.readline().rstrip('\n'))
            qin.put((i, n, expr))
    return t

def solveCCC2017(n, expr):
    e = defaultdict(list)
    d = defaultdict(int)
    for exp in expr:
        t = exp.split('=')
        _out = t[0]
        d[_out] += 0
        t = t[1].split('(')
        _in = t[1][:-1].split(',')
        for arg in _in:
            if arg.isspace() or arg == '':
                continue
            e[arg].append(_out)
            d[_out] += 1
    c = deque()
    for arg in d:
        if d[arg] == 0:
            c.append(arg)
    while len(c) > 0:
        _in = c.popleft()
        n -= 1
        for _out in e[_in]:
            d[_out] -= 1
            if d[_out] == 0:
                c.append(_out)
    if n == 0:
        return 'GOOD'
    else:
        return 'BAD'

def parseCCD2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            s = []
            for j in range(n):
                s.append(tuple(parseline(fin.readline().rstrip('\n'))))
            qin.put((i, n, s))
    return t

def solveCCD2017(n, s):
    a = sorted(s, key=lambda x: x[0])
    d = sorted(s, key=lambda x: x[1])
    p = n - 1
    q = n - 1
    removedSoilders = set()
    while p >= 0 or q >= 0:
        while p >= 0 and a[p] in removedSoilders:
            p -= 1
        while q >= 0 and d[q] in removedSoilders:
            q -= 1
        if p < 0 or q < 0:
            break
        t1 = set([a[p]])
        attack = a[p][0]
        p -= 1
        while p >= 0 and a[p][0] == attack:
            t1.add(a[p])
            p -= 1
        t2 = set([d[q]])
        defense = d[q][1]
        q -= 1
        while q >= 0 and d[q][1] == defense:
            t2.add(d[q])
            q -= 1
        if len(t1.intersection(t2)) > 0:
            return 'YES'
        removedSoilders = removedSoilders.union(t1).union(t2)
    return 'NO'