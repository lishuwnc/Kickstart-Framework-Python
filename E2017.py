from utility import *

def parseEA2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            s = fin.readline().rstrip('\n')
            qin.put((i, s))
    return t

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

def parseEB2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            L = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, L))
    return t

def solveEB2017(n, L):
    c = Counter(L)
    tmp = list(c.items())
    length, count = zip(*sorted(tmp))
    res = 0
    for i in range(len(length)):
        if count[i] < 2:
            continue
        p = 0
        tmp = 0
        s = 0
        ir = 0
        for q in range(len(length)):
            if q == i:
                continue
            if length[q] < 3 * length[i]:
                ir += count[q]
            while p < q and length[p] + 2 * length[i] <= length[q]:
                if p == i:
                    p += 1
                    continue
                s -= count[p]
                p += 1
            tmp += count[q] * s if q != i else (count[q] - 2) * s
            s += count[q] if q != i else count[q] - 2
        res += count[i] * (count[i] - 1) // 2 * tmp
        if count[i] >= 3:
            res += count[i] * (count[i] - 1) * (count[i] - 2) // 6 * ir
    return res

def parseEC2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            a = parseline(fin.readline().rstrip('\n'))
            b = parseline(fin.readline().rstrip('\n'))
            c = parseline(fin.readline().rstrip('\n'))
            qin.put((i, a, b, c))
    return t

def sovleEC(a, b, c):
    res = 2 ** 31
    p = [(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]
    for x, y, z in p:
        lo = 0
        hi = 2 ** 31
        while hi - lo >= 1e-6:
            mid = (lo + hi) / 2
            if isCircleCross(a, 3 * mid, b, mid, c, 3 * mid):
                hi = mid
            else:
                lo = mid
        res = min(res, (lo + hi) / 2)
