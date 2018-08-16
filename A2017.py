from utility import *

def parseAA2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            r, c = parseline(fin.readline().rstrip('\n'))
            qin.put((i, r, c))
    return t

def solveAA2017(r, c):
    r, c = min(r, c), max(r, c)
    res = r * c * r * (r - 1) // 2 % (10 ** 9 + 7)
    res = (res - (r + c) * (r ** 3 * 2  - r ** 2 * 3 + r) // 6) % (10 ** 9 + 7)
    res = (res + (r ** 4 - 2 * r ** 3 + r ** 2) // 4) % (10 ** 9 + 7)
    return res

def parseAB2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            p1 = list(fin.readline().rstrip('\n'))
            p2 = list(fin.readline().rstrip('\n'))
            qin.put((i, p1, p2))
    return t

def solveAB2017(p1, p2):
    n = len(p1)
    m = len(p2)
    res = [[False] * (m + 1) for i in range(n + 1)]
    res[0][0] = True
    for i in range(m):
        if p2[i] == '*':
            res[0][i + 1] = True
        else:
            break
    for i in range(n):
        if p1[i] == '*':
            res[i + 1][0] = True
        else:
            break
    for i in range(n):
        for j in range(m):
            if p1[i] != '*':
                if p2[j] != '*':
                    res[i + 1][j + 1] = (p1[i] == p2[j]) and res[i][j]
                else:
                    p = 0
                    k = 0
                    while p < 5:
                        if i - k + 1 < 0:
                            break
                        res[i + 1][j + 1] |= res[i - k + 1][j]
                        if i == k - 1:
                            p = 5
                        elif p1[i - k] != '*':
                            p += 1
                        k += 1
            else:
                if p2[j] != '*':
                    p = 0
                    k = 0
                    while p < 5:
                        if j - k + 1 < 0:
                            break
                        res[i + 1][j + 1] |= res[i][j - k + 1]
                        if j == k - 1:
                            p = 5
                        elif p2[j - k] != '*':
                            p += 1
                        k += 1
                else:
                    p = 0
                    k = 0
                    while p < 5:
                        if i - k + 1 < 0:
                            break
                        res[i + 1][j + 1] |= res[i - k + 1][j]
                        if i == k - 1:
                            p = 5
                        elif p1[i - k] != '*':
                            p += 1
                        k += 1
                    p = 0
                    k = 0
                    while p < 5:
                        if j - k + 1 < 0:
                            break
                        res[i + 1][j + 1] |= res[i][j - k + 1]
                        if j == k - 1:
                            p = 5
                        elif p2[j - k] != '*':
                            p += 1
                        k += 1
    return 'TRUE' if res[-1][-1] else 'FALSE'

def parseAC2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            c = []
            for j in range(n):
                c.append(parseline(fin.readline().rstrip('\n')))
            qin.put((i, n, c))
    return t

def solveAC2017(n, c):
    sx, sy, sz = 2 ** 31, 2 ** 31, 2 ** 31
    lx, ly, lz = -2 ** 31, -2 ** 31, -2 ** 31
    for i in range(len(c)):
        sx = min(sx, c[i][0] - c[i][3])
        sy = min(sy, c[i][1] - c[i][3])
        sz = min(sz, c[i][2] - c[i][3])
        lx = max(lx, c[i][0] + c[i][3])
        ly = max(ly, c[i][1] + c[i][3])
        lz = max(lz, c[i][2] + c[i][3])
    res = 2 ** 31

    lo = 0
    hi = 2 ** 31
    while lo <= hi:
        mid = (lo + hi) // 2
        f = True
        for i in range(len(c)):
            if (c[i][0] + c[i][3] - sx) <= mid and (c[i][1] + c[i][3] - sy) <= mid and (c[i][2] + c[i][3] - sz) <= mid:
                continue
            if (lx - c[i][0] + c[i][3]) <= mid and (ly - c[i][1] + c[i][3]) <= mid and (lz - c[i][2] + c[i][3]) <= mid:
                continue
            f = False
            break
        if f:
            hi = mid - 1
        else:
            lo = mid + 1
    res = min(res, lo)
    lo = 0
    hi = 2 ** 31
    while lo <= hi:
        mid = (lo + hi) // 2
        f = True
        for i in range(len(c)):
            if (c[i][0] + c[i][3] - sx) <= mid and (c[i][1] + c[i][3] - sy) <= mid and (lz - c[i][2] + c[i][3]) <= mid:
                continue
            if (lx - c[i][0] + c[i][3]) <= mid and (ly - c[i][1] + c[i][3]) <= mid and (c[i][2] + c[i][3] - sz) <= mid:
                continue
            f = False
            break
        if f:
            hi = mid - 1
        else:
            lo = mid + 1
    res = min(res, lo)
    lo = 0
    hi = 2 ** 31
    while lo <= hi:
        mid = (lo + hi) // 2
        f = True
        for i in range(len(c)):
            if (c[i][0] + c[i][3] - sx) <= mid and (ly - c[i][1] + c[i][3]) <= mid and (c[i][2] + c[i][3] - sz) <= mid:
                continue
            if (lx - c[i][0] + c[i][3]) <= mid and (c[i][1] + c[i][3] - sy) <= mid and (lz - c[i][2] + c[i][3]) <= mid:
                continue
            f = False
            break
        if f:
            hi = mid - 1
        else:
            lo = mid + 1
    res = min(res, lo)
    lo = 0
    hi = 2 ** 31
    while lo <= hi:
        mid = (lo + hi) // 2
        f = True
        for i in range(len(c)):
            if (lx - c[i][0] + c[i][3]) <= mid and (c[i][1] + c[i][3] - sy) <= mid and (c[i][2] + c[i][3] - sz) <= mid:
                continue
            if (c[i][0] + c[i][3] - sx) <= mid and (ly - c[i][1] + c[i][3]) <= mid and (lz - c[i][2] + c[i][3]) <= mid:
                continue
            f = False
            break
        if f:
            hi = mid - 1
        else:
            lo = mid + 1
    res = min(res, lo)
    return res