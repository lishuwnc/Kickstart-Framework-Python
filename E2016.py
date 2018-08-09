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
    print(t)
    return 0 * t[0] + (x & k) * t[1] + ((x & k) ^ k) * t[2] + k * t[3] + ((x | k) ^ k) * t[4] + x * t[5] + (x ^ k) * t[6] + (x | k) * t[7]
