from utility import *

def parseBA2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, m, k = parseline(fin.readline().rstrip('\n'))
            src, dst, cost = [], [], []
            for j in range(m):
                t1, t2 = parseline(fin.readline().rstrip('\n'))
                src.append(t1)
                dst.append(t2)
                cost.append(parseline(fin.readline().rstrip('\n')))
            D, S = [], []
            for j in range(k):
                d, s = parseline(fin.readline().rstrip('\n'))
                D.append(d)
                S.append(s)
            qin.put((i, n, m, k, src, dst, cost, D, S))
    return t

def solveBA2016(n, m, K, src, dst, cost, D, S):
    d = [[2 ** 31] * n for i in range(24)]
    visited = [[False] * n for i in range(24)]
    for i in range(24):
        d[i][0] = i
    e = defaultdict(set)
    for i in range(m):
        e[src[i] - 1].add((dst[i] - 1, i))
        e[dst[i] - 1].add((src[i] - 1, i))
    for i in range(24):
        for j in range(n):
            dist = 2 ** 31
            idx = 0
            for k in range(n):
                if not visited[i][k] and d[i][k] < dist:
                    dist = d[i][k]
                    idx = k
            visited[i][idx] = True
            for p, q in e[idx]:
                d[i][p] = min(d[i][p], d[i][idx] + cost[q][d[i][idx] % 24])
    res = []
    for i in range(K):
        res.append(d[S[i]][D[i] - 1] - S[i] if d[S[i]][D[i] - 1] < 2 ** 31 else -1)
    return ' '.join([str(v) for v in res])

def parseBB2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            fin.readline()
            np, ne, nt = parseline(fin.readline().rstrip('\n'))
            P = parseline(fin.readline().rstrip('\n'))
            E = parseline(fin.readline().rstrip('\n'))
            T = parseline(fin.readline().rstrip('\n'))
            A, B = [], []
            m = int(fin.readline().rstrip('\n'))
            for j in range(m):
                a, b = parseline(fin.readline().rstrip('\n'))
                A.append(a)
                B.append(b)
            qin.put((i, np, ne, nt, P, E, T, A, B, m))
    return t

def solveBB2016(np, ne, nt, P, E, T, A, B, m):
    c1 = [fractions.Fraction(p, t) for p in P for t in T]
    c2 = set([fractions.Fraction(e1, e2) for e1 in E for e2 in E])
    c2.remove(fractions.Fraction(1))
    res = []
    for i in range(m):
        f = False
        for v in c1:
            if fractions.Fraction(A[i], B[i]) / v in c2:
                f = True
                break
        if f:
            res.append('Yes')
        else:
            res.append('No')
    return '\n'.join(res)

def parseBC2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            qin.put((i, n))
    return t

def solveBC2016(n):
    t = math.ceil(math.sqrt(n))
    if t ** 2 < n:
        t += 1
    t = max(t, 1000)
    p = [True] * (t + 1)
    for i in range(2, t + 1):
        if not p[i]:
            continue
        for j in range(i, t + 1):
            if j * i > t:
                break
            else:
                p[j * i] = False

    c = []
    _n = n
    for v in range(2, t):
        if n % v == 0:
            c.append(1)
            while n % v == 0:
                c[-1] *= v
                n //= v
    if n != 1:
        c.append(n)
    m = {}
    def helper(n, c):
        if n in m:
            return m[n]
        t = 0
        _n = n
        while _n > 0:
            t += _n % 10
            _n //= 10
        if p[t]:
            m[n] = 0
            return 0
        _c = c[:]
        for v in c:
            _c.remove(v)
            res = helper(n // v, _c)
            if res == 0:
                m[n] = 1
                return 1
            _c.append(v)
        m[n] = 0
        return 0
    res = helper(_n, c)
    print(res)
    return 'Laurence' if res == 1 else 'Seymour'

def parseBD2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            s = fin.readline().rstrip('\n')
            qin.put((i, s))
    return t

def solveBD2016(s):
    res = [[[[0] * 4 for k in range(len(s) // 2 + 2)] for j in range(len(s) // 2 + 2)] for i in range(2)]
    res[0][0][0][3] = 1
    for i in range(1, len(s) + 1):
        f = i % 2
        for j in range(len(s) // 2 + 1):
            for k in range(len(s) // 2 + 1):
                for p in range(4):
                    res[f][j][k][p] = res[1 - f][j][k][p]
                    if p == 0:
                        if s[i - 1] == 'a' and k == 0:
                            if j > 1:
                                res[f][j][k][p] += res[1 - f][j - 1][k][p]
                            elif j == 1:
                                res[f][j][k][p] += res[1 - f][0][0][3]
                    elif p == 1:
                        if s[i - 1] == 'b' and j > 0:
                            if k > 1:
                                res[f][j][k][p] += res[1 - f][j][k - 1][p]
                            elif k == 1:
                                res[f][j][k][p] += res[1 - f][j][0][0]
                    elif p == 2:
                        if s[i - 1] == 'c' and k > 0:
                            if j <= len(s) // 2:
                                res[f][j][k][p] += res[1 - f][j + 1][k][2] + res[1 - f][j + 1][k][1]
                    else:
                        if s[i - 1] == 'd' and j == 0:
                            if k <= len(s) // 2:
                                res[f][j][k][p] += res[1 - f][0][k + 1][3] + res[1 - f][0][k + 1][2]
                    res[f][j][k][p] %= 10 ** 9 + 7
    print(res[len(s) % 2][0][0][3] - 1)
    return res[len(s) % 2][0][0][3] - 1