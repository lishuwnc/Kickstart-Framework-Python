from utility import *
import math

def parseAA2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            k = int(fin.readline().rstrip('\n'))
            qin.put((i, k))
    return t

def solveAA2016(k):
    n = math.ceil(math.log2(k + 1))
    if 2 ** n < k + 1:
        n += 1
    def helper(n, k):
        t = 0
        while n > 0:
            if k == 2 ** n:
                break
            if k < 2 ** n:
                n -= 1
            else:
                k = 2 ** (n + 1) - k
                n -= 1
                t = 1 - t
        return t
    return helper(n - 1, k)

def parseAB2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, m = parseline(fin.readline().rstrip('\n'))
            a = parseline(fin.readline().rstrip('\n'))
            L, R = [], []
            for j in range(m):
                l, r = parseline(fin.readline().rstrip('\n'))
                L.append(l)
                R.append(r)
            qin.put((i, n, m, a, L, R))
    return t

def solveAB2016(n, m, a, L, R):
    res = []
    for i in range(m):
        lo = 1
        hi = 10 ** 9
        while (hi - lo) > 1e-6:
            mid = (lo + hi) / 2
            t = 1
            for j in range(L[i], R[i] + 1):
                t *= a[j] / mid
            if t > 1:
                lo = mid
            elif t < 1:
                hi = mid
            else:
                break
        res.append(mid)
    return '\n'.join([str(v) for v in res])

def parseAC2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, m = parseline(fin.readline().rstrip('\n'))
            U, V, C = [], [], []
            for j in range(m):
                u, v, c = parseline(fin.readline().rstrip('\n'))
                U.append(u)
                V.append(v)
                C.append(c)
            qin.put((i, n, m, U, V, C))
    return t

def solveAC2016(n, m, U, V, C):
    d = [[2 ** 31] * n for i in range(n)]
    for i in range(m):
        d[U[i]][V[i]] = min(d[U[i]][V[i]], C[i])
        d[V[i]][U[i]] = min(d[U[i]][V[i]], C[i])
    for i in range(n):
        d[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    res = []
    for i in range(m):
        if d[U[i]][V[i]] < C[i]:
            res.append(i)
    return '\n'.join([str(v) for v in res])

def parseAD2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            s, r, c = parseline(fin.readline().rstrip('\n'))
            T, D = [], []
            for j in range(s):
                tick, d = parseline(fin.readline().rstrip('\n'), dtype_fn=str)
                T.append(int(tick))
                D.append(d)
            qin.put((i, s, r, c, T, D))
    return t

def solveAD2016(s, r, c, T, D):
    keypoints = deque([(0, 0), (0, 0)])
    directions = deque([1])
    grid = [[(i + j) % 2 for j in range(1, c + 1)] for i in range(1, r + 1)]
    delta = [-1, 0, 1, 0, -1]
    d = 1
    x, y = 0, 0
    grid[0][0] = -1
    idx = 0
    length = 1
    c = len(T)
    for t in range(10 ** 9):
        x = (x + delta[d]) % r
        y = (y + delta[d + 1]) % c
        fx, fy = keypoints.pop()
        keypoints.append((x, y))
        if grid[x][y] == 1:
            grid[x][y] = -1
            length += 1
        else:
            lx, ly = keypoints.popleft()
            grid[lx][ly] = 0
            _d = directions.popleft()
            lx = (lx + delta[_d]) % r
            ly = (ly + delta[_d + 1]) % c
            if lx != keypoints[0][0] or ly != keypoints[0][1]:
                directions.appendleft(_d)
                keypoints.appendleft((lx, ly))
            if grid[x][y] == -1:
                break
            grid[x][y] = -1
        if idx < c and T[idx] == t + 1:
            if D[idx] == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
            keypoints.append((x, y))
            directions.append(d)
            idx += 1
        if idx >= c and len(keypoints) == 2:
            break
    print(length)
    return length
