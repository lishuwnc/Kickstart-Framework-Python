from utility import *

def parseA(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, ts, tf = parseline(fin.readline().rstrip('\n'))
            s, f, d = [], [], []
            for j in range(n - 1):
                sj, fj, dj = parseline(fin.readline().rstrip('\n'))
                s.append(sj)
                f.append(fj)
                d.append(dj)
            qin.put((i, n, ts, tf, s, f, d))
    return t

def solveA(n, ts, tf, s, f, d):
    res = [[tf + 1] * (n) for i in range(n)]
    res[0][0] = 0
    for i in range(1, n):
        res[0][i] = (max(res[0][i - 1], s[i - 1]) - s[i - 1] + f[i - 1] - 1) // f[i - 1] * f[i - 1] + s[i - 1] + d[i - 1]
    if res[0][-1] <= tf:
        t = 0
        for i in range(1, n):
            for j in range(i, n):
                res[i][j] = min((max(res[i][j - 1], s[j - 1]) - s[j - 1] + f[j - 1] - 1) // f[j - 1] * f[j - 1] + s[j - 1] + d[j - 1],
                                (max(res[i - 1][j - 1] + ts, s[j - 1]) - s[j - 1] + f[j - 1] - 1) // f[j - 1] * f[j - 1] + s[j - 1] + d[j - 1])
            if res[i][-1] > tf:
                break
            else:
                t = i
        print(res)
        return t
    else:
        print(res)
        return 'IMPOSSIBLE'

def parseB(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, k, a1, b1, c, d, e1, e2, f = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, k, a1, b1, c, d, e1, e2, f))
    return t

def solveB(n, k, a1, b1, c, d, e1, e2, f):
    x = [a1]
    y = [b1]
    r = [0]
    s = [0]
    for i in range(1, n):
        _x, _y, _r, _s = x[-1], y[-1], r[-1], s[-1]
        x.append((c * _x + d * _y + e1) % f)
        y.append((c * _y + d * _x + e2) % f)
        r.append((c * _r + d * _s + e1) % f)
        s.append((c * _s + d * _r + e2) % f)
    a = [0] + [(-1) ** r[i] * x[i] for i in range(n)]
    b = [0] + [(-1) ** s[i] * y[i] for i in range(n)]
    for i in range(1, n + 1):
        a[i] += a[i - 1]
        b[i] += b[i - 1]

