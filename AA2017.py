from utility import *

def parseAAA2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            s = []
            for j in range(n):
                s.append(fin.readline().rstrip('\n'))
            qin.put((i, n, s))
    return t

def solveAAA2017(n, s):
    s.sort(key=lambda x: (-len(set(x) - set(' ')), x))
    return s[0]

def parseAAB2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            r, c = parseline(fin.readline().rstrip('\n'))
            grid = []
            for j in range(r):
                grid.append(parseline(fin.readline().rstrip('\n')))
            qin.put((i, r, c, grid))
    return t

def solveAAB2017(r, c, grid):
    h = [(grid[i][j], i, j) for i in range(r) for j in range(c)]
    h.sort()
    delta = [-1, 0, 1, 0, -1]
    res = 0
    for i in range(len(h)):
        minHeight = 2 ** 31
        _, x, y = h[i]
        height = grid[x][y]
        t = [(x, y, height)]
        grid[x][y] = 2 ** 31
        idx = 0
        while idx < len(t):
            x, y, _ = t[idx]
            for d in range(4):
                dx, dy = delta[d], delta[d + 1]
                if x + dx < 0 or x + dx >= r or y + dy < 0 or y + dy >= c or grid[x + dx][y + dy] < height:
                    minHeight = -1
                    idx = len(t)
                    break
                if grid[x + dx][y + dy] == height:
                    t.append((x + dx, y + dy, grid[x + dx][y + dy]))
                    grid[x + dx][y + dy] = 2 ** 31
                else:
                    minHeight = min(minHeight, grid[x + dx][y + dy])
            idx += 1
        if minHeight > 0:
            for x, y, _ in t:
                res += minHeight - height
                grid[x][y] = minHeight
        else:
            for x, y, height in t:
                grid[x][y] = height

    return res

def parseAAC2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            m = int(fin.readline().rstrip('\n'))
            c = parseline(fin.readline().rstrip('\n'))
            qin.put((i, m, c))
    return t

def solveAAC2017(m, c):
    if c[0] == sum(c[1:]):
        return 0
    if c[0] < sum(c[1:]):
        lo = 0
        hi = 1
        while hi - lo > 1e-9:
            mid = (lo + hi) / 2
            t = -c[0] * (1 + mid) ** m
            for i in range(1, m + 1):
                t += c[i] * (1 + mid) ** (m - i)
            if t > 0:
                lo = mid
            else:
                hi = mid
    else:
        lo = -1
        hi = 0
        while hi - lo > 1e-9:
            mid = (lo + hi) / 2
            t = -c[0] * (1 + mid) ** m
            for i in range(1, m + 1):
                t += c[i] * (1 + mid) ** (m - i)
            if t > 0:
                lo = mid
            else:
                hi = mid
    return mid

def parseAAD2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            m, n = parseline(fin.readline().rstrip('\n'))
            K, L, A, C = [], [], [], []
            for j in range(n):
                k, l = parseline(fin.readline().rstrip('\n'))
                K.append(k)
                L.append(l)
                A.append([0] + parseline(fin.readline().rstrip('\n')))
                if k > 1:
                    C.append([0, 0] + parseline(fin.readline().rstrip('\n')))
                else:
                    C.append([0, 0])
                    fin.readline()
            qin.put((i, m, n, K, L, A, C))
    return t

def solveAAD2017(m, n, K, L, A, C):
    card = []
    def helper(idx, target, tmp):
        if target == 0:
            card.append(tmp[:])
            return
        if idx >= n:
            return
        helper(idx + 1, target - 1, tmp + [idx])
        helper(idx + 1, target, tmp)
    helper(0, 8, [])
    res = 0
    for i in range(n):
        for j in range(1, K[i] + 1):
            C[i][j] += C[i][j - 1]
    for idx in card:
        t = []
        for i in range(L[idx[0]], K[idx[0]] + 1):
            for j in range(L[idx[1]], K[idx[1]] + 1):
                for p in range(L[idx[2]], K[idx[2]] + 1):
                    for q in range(L[idx[3]], K[idx[3]] + 1):
                        t.append((C[idx[0]][i] - C[idx[0]][L[idx[0]]] + C[idx[1]][j] - C[idx[1]][L[idx[1]]] + C[idx[2]][p] - C[idx[2]][L[idx[2]]] + C[idx[3]][q] - C[idx[3]][L[idx[3]]], A[idx[0]][i] + A[idx[1]][j] + A[idx[2]][p] + A[idx[3]][q]))
        t.sort()
        t, a = zip(*t)
        t = list(t)
        a = list(a)
        for i in range(1, len(a)):
            a[i] = max(a[i], a[i - 1])
        last = len(t) - 1
        for i in range(L[idx[4]], K[idx[4]] + 1):
            for j in range(L[idx[5]], K[idx[5]] + 1):
                for p in range(L[idx[6]], K[idx[6]] + 1):
                    for q in range(L[idx[7]], K[idx[7]] + 1):
                        cost = C[idx[4]][i] - C[idx[4]][L[idx[4]]] + C[idx[5]][j] - C[idx[6]][L[idx[6]]] + C[idx[6]][p] - C[idx[5]][L[idx[5]]] + C[idx[7]][q] - C[idx[7]][L[idx[7]]]
                        if cost > m:
                            continue
                        try:
                            res = max(res, a[bisect.bisect_left(t, m - cost + 1) - 1] + A[idx[4]][i] + A[idx[5]][j] + A[idx[6]][p] + A[idx[7]][q])
                        except IndexError:
                            pass
    return res