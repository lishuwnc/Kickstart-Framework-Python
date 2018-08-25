from utility import *

def parseFA2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            v = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, v))
    return t

def solveFA2017(n, v):
    p, q = 1, n
    if n % 2 == 1:
        a = n // 2
        if v[a] == p:
            p += 1
        elif v[a] == q:
            q -= 1
        else:
            return 'NO'
        a, b = a - 1, a + 1
        n -= 1
    else:
        a, b = n // 2 - 1, n // 2
    while n > 0:
        if n % 2 == 0:
            if v[a] == p:
                p += 1
            elif v[a] == q:
                q -= 1
            else:
                return 'NO'
            a -= 1
        else:
            if v[b] == p:
                p += 1
            elif v[b] == q:
                q -= 1
            else:
                return 'NO'
            b += 1
        n -= 1
    return 'YES'

def solveEA2017(s):
    n = len(s)
    res = [[[n] * (n + 1) for i in range(n)] for j in range(n + 1)]
    res[0][0][0] = 0
    #print(res[0])
    for idx in range(1, n + 1):
        res[idx][0][0] = res[idx - 1][0][0] + 1
        for start in range(idx):
            for offset in range(1, n):
                if start + offset > idx - offset:
                    break
                res[idx][start][offset] = min(res[idx - 1][start][offset] + 1, res[idx - 1][0][0] + 2)
                if s[start:start + offset] == s[idx - offset: idx]:
                    res[idx][start][offset] = min(res[idx][start][offset], res[idx - offset][start][offset] + 1, res[idx - offset][0][0] + 2)
                res[idx][0][0] = min(res[idx][0][0], res[idx][start][offset])
        for offset in range(1, idx + 1):
            res[idx][idx - offset][offset] = res[idx][0][0] + 1
        #print(res[idx])
    return res[n][0][0]

def parseFB2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            e, n = parseline(fin.readline().rstrip('\n'))
            s = parseline(fin.readline().rstrip('\n'))
            qin.put((i, e, n, s))
    return t

def solveFB2017(e, n, s):
    s.sort()
    res = 0
    p, q = 0, n - 1
    if e <= s[0]:
        return 0
    while p <= q:
        if e > s[p]:
            res += 1
            e -= s[p]
        elif p == q:
            pass
        else:
            e += s[q] - s[p]
            q -= 1
        p += 1
    return res

def parseFC2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, m, p = parseline(fin.readline().rstrip('\n'))
            u, v, d = [], [], []
            for j in range(m):
                _u, _v, _d = parseline(fin.readline().rstrip('\n'))
                u.append(_u)
                v.append(_v)
                d.append(_d)
            qin.put((i, n, m, p, u, v, d))
    return t

def solveFC2017(n, m, p, u, v, d):
    e = [[2 ** 31] * n for i in range(n)]
    for i in range(n):
        e[i][i] = 0
    for i in range(m):
        u[i] -= 1
        v[i] -= 1
        e[u[i]][v[i]] = d[i]
        e[v[i]][u[i]] = d[i]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                e[i][j] = min(e[i][j], e[i][k] + e[k][j])
    update_mat = np.array([[0] * (n + 1) for i in range(n + 1)], dtype=np.float)
    for i in range(n):
        for j in range(n):
            if i != j:
                update_mat[i][j] = 1 / (n - 1)
        update_mat[n][i] = sum(e[i]) / (n - 1)
    update_mat[n][n] = 1
    update_mat = fastPowMat(update_mat, p)
    res = update_mat[n][0]
    return res

def parseFD2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            qin.put((i, n))
    return t

def solveFD2017(n):
    res = [4] * (n + 1)
    res[0] = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j * j > i:
                break
            res[i] = min(res[i], res[i - j * j] + 1)
    return res[n]

