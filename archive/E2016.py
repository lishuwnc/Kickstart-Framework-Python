from utility import *

def parseEA2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            s = fin.readline().rstrip('\n')
            qin.put((i, s))
    return t

def solveEA2016(s):
    s = s[0] + s
    s = s + s[-1]
    res = 1
    for i in range(1, len(s) - 1):
        if s[i] == s[i - 1]:
            if s[i] == s[i + 1]:
                res = res * 1 % (10 ** 9 + 7)
            else:
                res = res * 2 % (10 ** 9 + 7)
        else:
            if s[i] == s[i + 1] or s[i - 1] == s[i + 1]:
                res = res * 2 % (10 ** 9 + 7)
            else:
                res = res * 3 % (10 ** 9 + 7)
    return res

def parseEB2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, k = parseline(fin.readline().rstrip('\n'))
            a = parseline(fin.readline().rstrip('\n'))
            b = parseline(fin.readline().rstrip('\n'))
            c = parseline(fin.readline().rstrip('\n'))
            d = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, k, a, b, c, d))
    return t

def solveEB2016(n, k, a, b, c, d):
    m = defaultdict(int)
    a = [v ^ k for v in a]
    for i in range(n):
        for j in range(n):
            m[a[i] ^ b[j]] += 1
    res = 0
    for i in range(n):
        for j in range(n):
            res += m[c[i] ^ d[j]]
    return res

def parseEC2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, x, k, a, b, c = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, x, k, a, b, c))
    return t

def solveEC2016(n, x, k, a, b, c):
    a /= 100
    b /= 100
    c /= 100
    t = [0, 0, 0, 0, 0, 1, 0, 0]
    for i in range(n):
        _t = [t[4] * a + t[3] * c + t[0] * a,
              t[5] * a + t[2] * c + t[1] * a,
              t[6] * a + t[1] * c + t[2] * a,
              t[3] * a + t[3] * b + t[0] * b + t[1] * b + t[2] * b + t[0] * c + t[7] * a,
              t[7] * c,
              t[6] * c,
              t[5] * c,
              t[7] * b + t[5] * b + t[6] * b + + t[4] * b + t[4] * c]
        t = _t
    return 0 * t[0] + (x & k) * t[1] + ((x & k) ^ k) * t[2] + k * t[3] + ((x | k) ^ k) * t[4] + x * t[5] + (x ^ k) * t[6] + (x | k) * t[7]

def parseED2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, q = parseline(fin.readline().rstrip('\n'))
            v = parseline(fin.readline().rstrip('\n'))
            l, r = [], []
            for j in range(q):
                t1, t2 = parseline(fin.readline().rstrip('\n'))
                l.append(t1)
                r.append(t2)
            qin.put((i, n, q, v, l, r))
    return t

def solveED2016(n, q, v, l, r):
    res = []
    v = [0] + v
    for i in range(1, n + 1):
        v[i] += v[i - 1]
    vv = v[:]
    for i in range(1, n + 1):
        vv[i] += vv[i - 1]
    for i in range(q):
        if l[i] - 1 <= 0:
            c1 = 0
        else:
            lo = 0
            hi = 2 ** 31
            c1 = 0
            while lo <= hi:
                mid = (lo + hi) // 2
                p_less = 1
                p_equal = 1
                less = 0
                equal = 0
                for j in range(n):
                    if p_less == j:
                        p_less += 1
                    if p_equal == j:
                        p_equal += 1
                    while p_equal <= n and v[p_equal] - v[j] <= mid:
                        p_equal += 1
                    while p_less <= n and v[p_less] - v[j] < mid:
                        p_less += 1
                    less += p_less - j - 1
                    equal += p_equal - p_less
                if less > l[i] - 1:
                    hi = mid - 1
                elif less + equal < l[i] - 1:
                    lo = mid + 1
                else:
                    break
            p = 1
            for j in range(n):
                if p == j:
                    p += 1
                while p <= n and v[p] - v[j] < mid:
                    p += 1
                c1 += vv[p - 1] - vv[j] - v[j] * (p - j - 1)
            c1 += mid * (l[i] - 1 - less)
        lo = 0
        hi = 2 ** 31
        c2 = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            p_less = 1
            p_equal = 1
            less = 0
            equal = 0
            for j in range(n):
                if p_less == j:
                    p_less += 1
                if p_equal == j:
                    p_equal += 1
                while p_equal <= n and v[p_equal] - v[j] <= mid:
                    p_equal += 1
                while p_less <= n and v[p_less] - v[j] < mid:
                    p_less += 1
                less += p_less - j - 1
                equal += p_equal - p_less
            if less > r[i]:
                hi = mid - 1
            elif less + equal < r[i]:
                lo = mid + 1
            else:
                break
        p = 1
        for j in range(n):
            if p == j:
                p += 1
            while p <= n and v[p] - v[j] < mid:
                p += 1
            c2 += vv[p - 1] - vv[j] - v[j] * (p - j - 1)
        c2 += mid * (r[i] - less)
        res.append(c2 - c1)
    return '\n'.join([str(x) for x in res])