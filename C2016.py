from utility import *

def parseCA2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            p = int(fin.readline().rstrip('\n'))
            s = parseline(fin.readline().rstrip('\n'))
            n = int(fin.readline().rstrip('\n'))
            W, Name = [], []
            for j in range(n):
                tmp = parseline(fin.readline().rstrip('\n'), dtype_fn=str)
                W.append(int(tmp[0]))
                Name.append(tmp[1:])
            m = int(fin.readline().rstrip('\n'))
            qin.put((i, p, s, n, W, Name, m))
    return t

def solveCA2016(p, s, n, W, Name, m):
    scores = defaultdict(list)
    for i in range(n):
        for j in range(p):
            scores[Name[i][j]].append(W[i] * s[j])
    total_score = []
    for a in scores:
        scores[a].sort(reverse=True)
        total_score.append((sum(scores[a][:m]), a))
    total_score.sort(key=lambda x: x[0], reverse=True)
    res = []
    c = []
    idx = 1
    ls = 2 ** 31
    total_score.append((-2**31, 'dummy'))
    for i in range(len(total_score)):
        if total_score[i][0] != ls:
            c.sort()
            for j in range(len(c)):
                res.append('{0}: {1}'.format(idx, c[j]))
            ls = total_score[i][0]
            idx += len(c)
            c = [total_score[i][1]]
        else:
            c.append(total_score[i][1])
    return '\n'.join(res)

def parseCB2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            P, K = [], []
            for j in range(n):
                p, k = parseline(fin.readline().rstrip('\n'))
                P.append(p)
                K.append(k)
            qin.put((i, n, P, K))
    return t

def solveCB2016(n, P, K):
    lo = 1
    hi = 10 ** 16
    for i in range(n):
        if P[i] != 0:
            hi = min(hi, round(K[i] * 100 / P[i]))
        if P[i] != 100:
            lo = max(lo, int(math.ceil(K[i] * 100 / (P[i] + 1))))
            while lo * (P[i] + 1) <= 100 * K[i]:
                lo += 1
        else:
            return K[i]
    if lo == hi:
        return lo
    else:
        return -1

def parseCC2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, m = parseline(fin.readline().rstrip('\n'))
            E, K, B = [], [], []
            _m = 0
            for j in range(m):
                e, k, b = parseline(fin.readline().rstrip('\n'))
                _m += b
                b = parseline(fin.readline().rstrip('\n'))
                for p in range(len(b)):
                    E.append(e - 1)
                    K.append(k)
                    B.append(b[p] - 1)
            qin.put((i, n, _m, E, K, B))
    return t

def solveCC2016(n, m, E, K, B):
    res = [None] * (2 ** (2 ** n))
    for i in range(2 ** (2 ** n)):
        c = []
        for j in range(16):
            if i & (1 << j) > 0:
                c.append(j)
        if len(c) == 1:
            res[i] = True
        elif len(c) not in [2, 4, 8, 16]:
            res[i] = False
        else:
            t = round(math.log2(len(c)))
            for j in range(m):
                if K[j] != t:
                    continue
                if E[j] not in c or B[j] not in c:
                    continue
                res[i] = False
                break
            if res[i] is None:
                res[i] = False
                for j in range(1, i):
                    if res[j] and res[i ^ j]:
                        res[i] = True
                        break
    print(n)
    if res[2 ** (2 ** n) - 1]:
        return 'YES'
    else:
        return 'NO'


def parseCD2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, k, c, x = parseline(fin.readline().rstrip('\n'))
            a = parseline(fin.readline().rstrip('\n'))
            b = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, k, c, x, a, b))
    return t

def solveCD2016(n, k, c, x, a, b):
    res = [[[(a[i] * (i + 1) + b[j] * (j + 1) + c) % x for j in range(n)] for i in range(n)] for k in range(2)]
    k = bin(k)[3:]
    t = 1
    p = 0
    for c in k:
        p = 1 - p
        if c == '0':
            for i in range(n - 2 * t + 1):
                for j in range(n - 2 * t + 1):
                    res[p][i][j] = max(res[1 - p][i][j], res[1 - p][i + t][j], res[1 - p][i][j + t], res[1 - p][i + t][j + t])
            t *= 2
        else:
            for i in range(n - 2 * t):
                for j in range(n - 2 * t):
                    res[p][i][j] = max(res[1 - p][i][j], res[1 - p][i + t][j], res[1 - p][i][j + t], res[1 - p][i + t][j + t], res[1 - p][i + t + 1][j], res[1 - p][i][j + t + 1], res[1 - p][i + t + 1][j + t + 1])
                    res[p][i][j] = max(res[p][i][j], res[1 - p][i + t][j + t + 1], res[1 - p][i + t + 1][j + t])
            t = t * 2 + 1
    s = 0
    for i in range(n - t + 1):
        for j in range(n - t + 1):
            s += res[p][i][j]
    return s
