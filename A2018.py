from utility import *

def parseAA2018(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            qin.put((i, n))
    return t

def solveAA2018(n):
    res = 0
    i = 0
    t = 0
    m = -1
    while n > 0:
        v = n % 10
        t = t + v * (10 ** i)
        n //= 10
        if v % 2 > 0:
            m = i
        i += 1
    if m < 0:
        res = 0
    else:
        v = (t // 10 ** m) % 10
        if v == 9:
            res = t % (10 ** m) + 1 + int('1' * m if m > 0 else '0')
        else:
            res = min(t % (10 ** m) + 1 + int('1' * m if m > 0 else '0'), 10 ** m - (t % (10 ** m)))
    return res

def parseAB2018(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, k = parseline(fin.readline().rstrip('\n'))
            v = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, k, v))
    return t

def solveAB2018(n, k, v):
    res = [0] * (k + 1)
    v.sort()
    s = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        s[i] = s[i + 1] + v[i]
    res[0] = sum(v) / n
    for i in range(1, k + 1):
        idx = bisect.bisect_right(v, res[i - 1])
        if idx == n:
            return res[i - 1]
        if abs(v[idx] - res[i - 1]) < 1e-6:
            idx += 1
        res[i] = idx / n * res[i - 1] + s[idx] / n
    return res[k]

def parseAC2018(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            L = int(fin.readline().rstrip('\n'))
            words = parseline(fin.readline().rstrip('\n'), dtype_fn=str)
            args = parseline(fin.readline().rstrip('\n'), dtype_fn=str)
            qin.put((i, L, words, args))
    return t

def solveAC2018(L, words, args):
    s1, s2 = args[0], args[1]
    N, A, B, C, D = int(args[2]), int(args[3]), int(args[4]), int(args[5]), int(args[6])
    x = [0] * N
    x[0] = ord(s1)
    x[1] = ord(s2)
    for i in range(2, N):
        x[i] = (A * x[i - 1] + B * x[i - 2] + C) % D
    s = [chr(97 + x[i] % 26) for i in range(N)]
    s[0] = s1
    s[1] = s2
    print(s)
    d = defaultdict(list)
    def count(w):
        ret = [0] * 26
        for c in w:
            ret[ord(c) - 97] += 1
        return ret
    visited = [False] * L
    for i in range(len(words)):
        w = words[i]
        d[w[0]].append((w[-1], len(w), count(w), i))
    res = 0
    tmp = [[0] * 26 for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(26):
            tmp[i][j] = tmp[i - 1][j]
        tmp[i][ord(s[i - 1]) - 97] += 1
    for i in range(N):
        for c, length, _count, idx in d[s[i]]:
            if visited[idx] or i + length - 1 >= N or s[i + length - 1] != c:
                continue
            f = True
            for j in range(26):
                if _count[j] != tmp[i + length][j] - tmp[i][j]:
                    f = False
                    break
            if not f:
                continue
            res += 1
            visited[idx] = True
    return res