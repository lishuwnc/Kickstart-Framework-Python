from utility import *

def parseEEA2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            s = fin.readline().rstrip('\n')
            n, m = parseline(fin.readline().rstrip('\n'))
            qin.put((i, s, n, m))
    return t

def solveEEA2017(s, n, m):
    t = [0] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        t[i] = t[i - 1]
        if s[i - 1] == 'B':
            t[i] += 1
    res = 0
    while (n - 1) % len(s) != 0:
        res += 1 if s[(n - 1) % len(s)] == 'B' else 0
        n += 1
    m += 1
    res += (m - n) // len(s) * t[-1]
    res += t[(m - 1) % len(s)]
    return res

def parseEEB2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            qin.put((i, n))
    return t

def solveEEB2017(n):
    q = 2
    p = 64
    while p > 2:
        lo = 2
        hi = n // p
        while lo <= hi:
            mid = (lo + hi) // 2
            t = (mid ** p - 1) - (mid - 1) * n
            if t == 0:
                return mid
            if t > 0:
                hi = mid - 1
            else:
                lo = mid + 1
        p -= 1
    return n - 1

def parseEEC2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, d = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, d))
    return t

def solveEEC2017(n, d):
    res = 0
    a = d
    while a <= n:
        m = 1
        while True:
            p = n - a - a * (m - 1)
            if p < 0:
                break
            q = m - 1
            if q < p / 2:
                res += 0
            elif q >= p:
                res += p // 2 + 1
            else:
                res += p // 2 - (p - q) + 1
            m += 1
        a += d
    return res