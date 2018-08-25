from utility import *

def parseDDA2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, m = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, m))
    return t

def solveDDA2017(n, m):
    return 1 - 2 * m / (n + m)

def parseDDB2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            r, c = parseline(fin.readline().rstrip('\n'))
            qin.put((i, r, c))
    return t

def solveDDB2017(r, c):
    if r > c:
        r, c = c, r
    k = c - c // 3
    res = 0
    res += r // 3 * 2 * c
    if r % 3 == 1:
        res += k
    elif r % 3 == 2:
        if r == 2 or c % 3 <= 1:
            res += 2 * k
        else:
            res += 2 * k - 1
    return res

def parseDDC2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            v, s = parseline(fin.readline().rstrip('\n'))
            d = []
            for j in range(v):
                d.append(fin.readline().rstrip('\n'))
            q = []
            for j in range(s):
                q.append(fin.readline().rstrip('\n'))
            qin.put((i, v, s, d, q))
    return t

def solveDDC2017(v, s, d, q):
    c = defaultdict(int)
    for t in d:
        x = [0] * 26
        for w in t:
            x[ord(w) - ord('a')] += 1
        c[tuple(x)] += 1
    m = max([len(t) for t in d])
    res = []
    for i in range(s):
        t = [0] * (len(q[i]) + 1)
        t[0] = 1
        for j in range(1, len(q[i]) + 1):
            _c = [0] * 26
            for k in range(j - 1, max(-1, j - 1 - m), -1):
                _c[ord(q[i][k]) - ord('a')] += 1
                if tuple(_c) in c:
                    t[j] = (t[j] + t[k] * c[tuple(_c)]) % (10 ** 9 + 7)
        res.append(t[-1])
    return ' '.join([str(v) for v in res])

def parseDDD2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, m, l = parseline(fin.readline().rstrip('\n'))
            a, b, p = [], [], []
            for j in range(n):
                t1, t2, t3 = parseline(fin.readline().rstrip('\n'))
                a.append(t1)
                b.append(t2)
                p.append(t3)
            qin.put((i, n, m, l, a, b, p))
    return t

def solveDDD2017(n, m, l, a, b, p):
    res = [2 ** 31] * (1 + l)
    res[0] = 0
    for i in range(n):
        t = deque()
        if a[i] > l:
            continue
        for j in range(l - a[i], max(-1, l - b[i] - 1), -1):
            while len(t) > 0 and t[-1][0] >= res[j]:
                t.pop()
            t.append((res[j], j))
        for j in range(l, a[i] - 1, -1):
            res[j] = min(res[j], t[0][0] + p[i])
            if t[0][1] == j - a[i]:
                t.popleft()
            if j - b[i] - 1 >= 0:
                while len(t) > 0 and t[-1][0] >= res[j - b[i] - 1]:
                    t.pop()
                t.append((res[j - b[i] - 1], j - b[i] - 1))
    return res[l] if res[l] < m else 'IMPOSSIBLE'