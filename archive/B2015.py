from utility import *

def parseBA2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            m, n = parseline(fin.readline().rstrip('\n'))
            qin.put((i, m, n))
    return t

def solveBA2015(m, n):
    if m == 1:
        return 1
    t = [0] * (m + 1)
    t[1] = 1
    for i in range(2, m + 1):
        t[i] = fastPow(i, n)
        for j in range(1, i):
            t[i] -= t[j] * nCr(i, j)
            if t[i] < 0:
                t[i] += 10 ** 9 + 7
    return t[-1] % (10 ** 9 + 7)

def parseBB2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            b, l, n = parseline(fin.readline().rstrip('\n'))
            qin.put((i, b, l, n))
    return t

def solveBB2015(b, l, n):
    t = 1
    n -= 1
    while n - t >= 0:
        n -= t
        t += 1
    m = {}

    def helper(l, t, n):
        if (l, t, n) in m:
            return m[(l, t, n)]
        if l == 1:
            return b * 750
        res = 0
        if t < l:
            res += max(0, (helper(l - 1, t, n) - 250) / 3)
        if n > 0:
            res += max(0, (helper(l - 1, t - 1, n - 1) - 250) / 3)
        if n != t - 1:
            res += max(0, (helper(l - 1, t - 1, n) - 250) / 3)
        m[(l, t, n)] = res
        return res

    res = min(helper(l, t, n), 250)
    return res

def parseBC2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, k = parseline(fin.readline().rstrip('\n'))
            a = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, k ,a))
    return t

def solveBC2015(n, k, a):
    res = [[None] * n for i in range(n)]
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            res[j][j + i - 1] = i
            if i < 3:
                continue
            res[j][j + i - 1] = min(res[j][j + i - 1], res[j + 1][j + i - 1] + 1)
            for k1 in range(j + 1, j + i - 1):
                if a[k1] - a[j] != k or (k1 != j + 1 and res[j + 1][k1 - 1] > 0):
                    continue
                for k2 in range(k1 + 1, j + i):
                    if a[k2] - a[k1] != k or (k2 != k1 + 1 and res[k1 + 1][k2 - 1] > 0):
                        continue
                    res[j][j + i - 1] = min(res[j][j + i - 1], res[k2 + 1][j + i - 1] if k2 < j + i - 1 else 0)
    return res[0][n - 1]

def parseBD2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, k = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, k))
    return t

'''
def solveBD2015(n, k):
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    a[1] = 1
    b[1] = 1
    for i in range(2, n + 1):
        a[i] = b[i - 1]
        for j in range(1, i):
            b[i] += a[j] * b[i - j]
        b[i] += a[i]
        if b[i] >= k:
            break
    if b[n] < k and i == n:
        return 'Doesn\'t Exist!'
    res = [None] * (2 * n)
    surrounding = n - i
    _i = i
    for i in range(surrounding):
        res[i] = '('
        res[-i - 1] = ')'
    a[0] = 1
    b[0] = 1
    k -= 1
    def fillRes(start, end, a, b, n, k, res):
        if start >= end:
            return res
        if start + 1 == end:
            res[start] = '('
            res[end] = ')'
            return res
        i = n
        while a[i] * b[n - i] <= k:
            k -= a[i] * b[n - i]
            i -= 1
        res[start] = '('
        res[start + 2 * i - 1] = ')'
        res = fillRes(start + 1, start + 2 * i - 2, a, b, i - 1, k // b[n - i], res)
        res = fillRes(start + 2 * i, end, a, b, n - i, k % b[n - i], res)
        return res
    res = fillRes(surrounding, 2 * n - surrounding - 1, a, b, _i, k, res)
    return ''.join(res)
'''

def solveBD2015(n, k):
    res = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n + 1):
        res[0][i] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            res[i][j] = res[i - 1][j] + (res[i][j - 1] if i < j else 0)
    i, j = n, n
    s = ''
    if k > res[n][n]:
        return 'Doesn\'t Exist!'
    while i > 0 or j > 0:
        if i > 0 and res[i - 1][j] >= k:
            s += '('
            i -= 1
        else:
            s += ')'
            k -= res[i - 1][j]
            j -= 1
    return s