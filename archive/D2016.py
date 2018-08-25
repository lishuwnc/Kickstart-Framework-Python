from utility import *

def parseDA2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            r, c = parseline(fin.readline().rstrip('\n'))
            grid = []
            for j in range(r):
                grid.append(list(fin.readline().rstrip('\n')))
            n = int(fin.readline().rstrip('\n'))
            q = []
            for j in range(n):
                q.append(fin.readline().rstrip('\n'))
            qin.put((i, r, c, grid, n, q))
    return t

def solveDA2016(r, c, grid, n, q):
    delta = [-1, 0, 1, 0, -1]
    res = []
    def helper():
        t = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] != '1':
                    continue
                t += 1
                queue = deque()
                queue.append((i, j))
                grid[i][j] = '.'
                qsize = 1
                while qsize > 0:
                    x, y = queue.popleft()
                    qsize -= 1
                    for d in range(4):
                        dx, dy = delta[d], delta[d + 1]
                        if x + dx >= 0 and x + dx < r and y + dy >= 0 and y + dy < c and grid[x + dx][y + dy] == '1':
                            qsize += 1
                            grid[x + dx][y + dy] = '.'
                            queue.append((x + dx, y + dy))
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '.':
                    grid[i][j] = '1'
        return t

    for i in range(n):
        query = q[i]
        if query[0] == 'Q':
            res.append(helper())
        else:
            args = query.split()
            x = int(args[1])
            y = int(args[2])
            z = args[3]
            grid[x][y] = z
    return '\n'.join([str(v) for v in res])

def parseDB2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, m, q = parseline(fin.readline().rstrip('\n'))
            v = parseline(fin.readline().rstrip('\n'))
            p, h = [], []
            _n = n
            for j in range(n):
                t1, t2 = parseline(fin.readline().rstrip('\n'))
                if t1 == 0:
                    _n -= 1
                    continue
                p.append(t1)
                h.append(t2)
            qin.put((i, _n, m, q, v, p, h))
    return t

def solveDB2016(n, m, q, v, p, h):
    t = [2 ** 31 if p[i] * v[h[i]] >= 0 else math.ceil(p[i] / -v[h[i]]) for i in range(n)]
    c = SortedList(zip(t, range(n), [0] * n))
    while True:
        t, idx, cost = c.pop()
        _t = t
        while h[idx] - (cost + 1) >= 0 or h[idx] + (cost + 1) < m:
            cost += 1
            q -= 1
            if q < 0:
                break
            if h[idx] - cost >= 0:
                t = min(t, 2 ** 31 if p[idx] * v[h[idx] - cost] >= 0 else math.ceil(p[idx] / -v[h[idx] - cost]))
            if h[idx] + cost < m:
                t = min(t, 2 ** 31 if p[idx] * v[h[idx] + cost] >= 0 else math.ceil(p[idx] / -v[h[idx] + cost]))
            if t < _t:
                break
        c.add((t, idx, cost))
        if q < 0 or t == _t:
            break
    if c[-1][0] == 2 ** 31:
        return 'IMPOSSIBLE'
    else:
        return c[-1][0]

def parseDC2016(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            q = []
            for j in range(n):
                q.append(fin.readline().rstrip('\n'))
            qin.put((i, n, q))
    return t

class SubnetNode:
    def __init__(self, v, p):
        self.v = v
        self.isSubnet = False
        self.lc = None
        self.rc = None
        self.p = p

def solveDC2016(n, subnets):
    root = SubnetNode(0, None)
    for i in range(n):
        q = subnets[i]
        p = root
        q = q.split('.')
        a, b, c = int(q[0]), int(q[1]), int(q[2])
        q = q[3].split('/')
        d = int(q[0])
        e = int(q[1])
        s = (a << 24) + (b << 16) + (c << 8) + d
        s = bin(s)[2:]
        s = '0' * (32 - len(s)) + s
        for j in range(e):
            if p.isSubnet:
                break
            if s[j] == '0':
                if not p.lc:
                    p.lc = SubnetNode(0, p)
                p = p.lc
            else:
                if not p.rc:
                    p.rc = SubnetNode(1, p)
                p = p.rc
        p.isSubnet = True
        while p.p:
            if p is p.p.lc and p.p.rc and p.p.rc.isSubnet:
                p = p.p
            elif p is p.p.rc and p.p.lc and p.p.lc.isSubnet:
                p = p.p
            else:
                break
            p.isSubnet = True
    res = []
    def helper(root, s, depth, res):
        if not root:
            return
        if root.isSubnet:
            s = (s << 1) + root.v
            s = s << (32 - depth)
            a = s >> 24
            b = (s >> 16) % 256
            c = (s >> 8) % 256
            d = s % 256
            p = depth
            res.append('{0}.{1}.{2}.{3}/{4}'.format(a, b, c, d, p))
        else:
            helper(root.lc, (s << 1) + root.v, depth + 1, res)
            helper(root.rc, (s << 1) + root.v, depth + 1, res)
    helper(root, 0, 0, res)
    return '\n'.join(res)