from utility import *

def parseBBA2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            l, r = parseline(fin.readline().rstrip('\n'))
            qin.put((i, l, r))
    return t

def solveBBA2017(l, r):
    m = min(l, r)
    return m * (m + 1) // 2

def parseBBB2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            a, b, n, k = parseline(fin.readline().rstrip('\n'))
            qin.put((i, a, b, n, k))
    return t

def solveBBB2017(a, b, n, k):
    res = 0
    c1 = [0] * k
    for i in range(1, n % k + 1):
        c1[fastPow(i, a, k)] += 1
    for i in range(k):
        t = fastPow(i, a, k)
        c1[t] += n // k
    c2 = [0] * k
    for i in range(1, n % k + 1):
        c2[fastPow(i, b, k)] += 1
    for i in range(k):
        c2[fastPow(i, b, k)] += n // k
    c3 = 0
    for i in range(1, n % k + 1):
        if (fastPow(i, a, k) + fastPow(i, b, k)) % k == 0:
            c3 += 1
    for i in range(k):
        if (fastPow(i, a, k) + fastPow(i, b, k)) % k == 0:
            c3 += n // k
    for i in range(1, k):
        res = (res + c1[i] * c2[k - i]) % (10 ** 9 + 7)
    res += c1[0] * c2[0] - c3
    return res % (10 ** 9 + 7)

def parseBBC2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, l, r, a, b, c1, c2, m = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, l, r, a, b, c1, c2, m))
    return t

def solveBBC2017(n, l, r, a, b, c1, c2, m):
    X = [l]
    Y = [r]
    L = [l]
    R = [r]
    for i in range(1, n):
        x, y = (a * X[-1] + b * Y[-1] + c1) % m, (a * Y[-1] + b * X[-1] + c2) % m
        X.append(x)
        Y.append(y)
        l, r = min(x, y), max(x, y)
        L.append(l)
        R.append(r)
    t = [(L[i], 1, i) for i in range(n)] + [(R[i] + 1, -1, i) for i in range(n)]
    t.sort()
    s = 0
    area = 0
    p = 0
    x = None
    flag = 0
    interval = set()
    c = 0
    lc = -1
    for i in range(len(t)):
        v, d, idx = t[i]
        if s == 1 and flag != v:
            _lc = interval.pop()
            if _lc == lc:
                c += v - t[i - 1][0]
            else:
                lc = _lc
                p = max(p, c)
                c = v - t[i - 1][0]
            interval.add(_lc)
        s += d
        if d < 0:
            flag = v
            interval.remove(idx)
        else:
            interval.add(idx)
        if s == 0:
            area += v - x
            x = None
        else:
            if x is None:
                x = v
    p = max(p, c)
    return area - p

def parseBBD2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, m = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, m))
    return t

def solveBBD2017(n, m):
    cache = [0] * (n + 1)
    for i in range(0, n + 1):
        cache[i] = factorial(i, m)
    pri = [0] * (n + 1)
    pri[1] = 1
    for i in range(2, n + 1):
        pri[i] = factorial(i, m)
        for j in range(1, i):
            pri[i] = (pri[i] - cache[i - j] * pri[j]) % m
    res = [0] * (n + 1)
    s = [0] * (n + 1)
    res[1] = 1
    s[1] = 1
    for i in range(2, n + 1):
        for j in range(0, i + 1):
            res[i] += (res[j] + 2 * s[j] + cache[j]) * pri[i - j]
            s[i] += (s[j] + cache[j]) * pri[i - j]
            res[i] %= m
            s[i] %= m
    return res[n] % m