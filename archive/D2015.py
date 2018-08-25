from utility import *

def parseDA2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            grid = []
            for j in range(n):
                grid.append(parseline(fin.readline().rstrip('\n')))
            qin.put((i, n, grid))
    return t

def solveDA2015(n, grid):
    step = 1
    room = 1
    delta = [-1, 0, 1, 0, -1]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                continue
            q = deque()
            _z = grid[i][j]
            q.append((i, j, _z))
            grid[i][j] = -1
            t = 1
            while len(q) > 0:
                x, y, z = q.popleft()
                for d in range(4):
                    dx, dy = delta[d], delta[d + 1]
                    if x + dx >= 0 and x + dx < n and y + dy >= 0 and y + dy < n and grid[x + dx][y + dy] == z + 1:
                        grid[x + dx][y + dy] = -1
                        q.append((x + dx, y + dy, z + 1))
                        t += 1
            q.append((i, j, _z))
            while len(q) > 0:
                x, y, z = q.popleft()
                for d in range(4):
                    dx, dy = delta[d], delta[d + 1]
                    if x + dx >= 0 and x + dx < n and y + dy >= 0 and y + dy < n and grid[x + dx][y + dy] == z - 1:
                        grid[x + dx][y + dy] = -1
                        q.append((x + dx, y + dy, z - 1))
                        _z -= 1
                        t += 1
            if t > step:
                step = t
                room = _z
            elif t == step:
                room = min(room, _z)

    return '{0} {1}'.format(room, step)

def parseDB2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            v = parseline(fin.readline().rstrip('\n'))
            p = int(fin.readline().rstrip('\n'))
            p_num = []
            for j in range(p):
                p_num.append(int(fin.readline().rstrip('\n')))
            fin.readline()
            qin.put((i, n, v, p, p_num))
    return t

def solveDB2015(n, v, p, p_num):
    a = [(x, 1) for x in v[0::2]]
    b = [(x + 1, -1) for x in v[1::2]]
    v = sorted(a + b)
    s = 0
    idx = 0
    for i in range(len(v)):
        x, d = v[i]
        s += d
        if x > v[idx][0]:
            idx += 1
        v[idx] = (x, s)
    x, s = zip(*v[:idx + 1])
    res = []
    for p in p_num:
        idx = bisect.bisect_left(x, p)
        if idx >= len(x):
            res.append(0)
        elif p == x[idx]:
            res.append(s[idx])
        elif idx == 0:
            res.append(0)
        else:
            res.append(s[idx - 1])
    return ' '.join([str(v) for v in res])

def parseDC2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            src = []
            dst = []
            for j in range(n):
                src.append(fin.readline().rstrip('\n'))
                dst.append(fin.readline().rstrip('\n'))
            qin.put((i, n, src, dst))
    return t

def solveDC2015(n, src, dst):
    m = {}
    d = defaultdict(int)
    for i in range(n):
        m[src[i]] = dst[i]
        d[src[i]] += 1
        d[dst[i]] -= 1
    for t in d:
        if d[t] == 1:
            break
    res = []
    while True:
        res.append('{0}-{1}'.format(t, m[t]))
        t = m[t]
        if t not in m:
            break
    return ' '.join(res)

def parseDD2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            pieces = []
            for j in range(n):
                pieces.append(fin.readline().rstrip('\n'))
            qin.put((i, n, pieces))
    return t

def solveDD2015(n, pieces):
    res = 0
    grid = [[None] * 8 for i in range(8)]
    for i in range(n):
        x = ord(pieces[i][0]) - ord('A')
        y = int(pieces[i][1]) - 1
        t = pieces[i][3]
        grid[x][y] = t
    for i in range(8):
        for j in range(8):
            if grid[i][j] is None:
                continue
            if grid[i][j] == 'K':
                delta = [-1, 0, 1, 0, -1, 1, 1, -1, -1]
                for d in range(8):
                    dx, dy = delta[d], delta[d + 1]
                    if i + dx >= 0 and i + dx < 8 and j + dy >= 0 and j + dy < 8 and grid[i + dx][j + dy] is not None:
                        res += 1
            elif grid[i][j] == 'Q':
                delta = [-1, 0, 1, 0, -1, 1, 1, -1, -1]
                for d in range(8):
                    dx, dy = delta[d], delta[d + 1]
                    t = 1
                    while i + t * dx >= 0 and i + t * dx < 8 and j + t * dy >= 0 and j + t * dy < 8:
                        if grid[i + t * dx][j + t * dy] is not None:
                            res += 1
                            break
                        t += 1
            elif grid[i][j] == 'R':
                delta = [-1, 0, 1, 0, -1]
                for d in range(4):
                    dx, dy = delta[d], delta[d + 1]
                    t = 1
                    while i + t * dx >= 0 and i + t * dx < 8 and j + t * dy >= 0 and j + t * dy < 8:
                        if grid[i + t * dx][j + t * dy] is not None:
                            res += 1
                            break
                        t += 1
            elif grid[i][j] == 'B':
                delta = [-1, 1, 1, -1, -1]
                for d in range(4):
                    dx, dy = delta[d], delta[d + 1]
                    t = 1
                    while i + t * dx >= 0 and i + t * dx < 8 and j + t * dy >= 0 and j + t * dy < 8:
                        if grid[i + t * dx][j + t * dy] is not None:
                            res += 1
                            break
                        t += 1
            elif grid[i][j] == 'N':
                delta = [-1, 2, 1, -2, -1, -2, 1, 2, -1]
                for d in range(8):
                    dx, dy = delta[d], delta[d + 1]
                    if i + dx >= 0 and i + dx < 8 and j + dy >= 0 and j + dy < 8 and grid[i + dx][j + dy] is not None:
                            res += 1
            else:
                if i + 1 >= 0 and i + 1 < 8:
                    if j + 1 >= 0 and j + 1 < 8 and grid[i + 1][j + 1] is not None:
                        res += 1
                    if j - 1 >= 0 and j - 1 < 8 and grid[i + 1][j - 1] is not None:
                        res += 1
    return res