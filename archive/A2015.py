from utility import *

def parseAA2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            s = parseline(fin.readline().rstrip('\n'), dtype_fn=str)
            n = int(s[0])
            v = [int(x, base=2) for x in s[1:]]
            qin.put((i, n, v))
    return t

def solveAA2015(n, v):
    m = {0: int('1111110', 2),
         1: int('0110000', 2),
         2: int('1101101', 2),
         3: int('1111001', 2),
         4: int('0110011', 2),
         5: int('1011011', 2),
         6: int('1011111', 2),
         7: int('1110000', 2),
         8: int('1111111', 2),
         9: int('1111011', 2)
    }
    res = []
    for i in range(10):
        t = i
        broken = 0
        normal = 0
        p = True
        for j in range(n):
            if v[j] | m[t] != m[t] or v[j] & broken > 0:
                p = False
                break
            broken |= v[j] ^ m[t]
            normal |= v[j]
            t -= 1
            if t < 0:
                t = 9
        if p:
            for j in range(n):
                if v[j] & broken > 0:
                    p = False
                    break
        if p:
            s = i - n
            while s < 0:
                s += 10
            res.append((i, broken, normal))
    if len(res) == 0:
        return 'ERROR!'
    else:
        tmp = set()
        for r in res:
            s, broken, normal = r
            s = s - n
            while s < 0:
                s += 10
            if ((m[s] & ~broken) | normal) != normal:
                return 'ERROR!'
            tmp.add(bin(m[s] & ~broken)[2:])
        if len(tmp) > 1:
            return 'ERROR!'
        res = list(tmp)[0]
        return '0' * (7 - len(res)) + res

def parseAB2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            s = parseline(fin.readline().rstrip('\n'), dtype_fn=str)
            n = int(s[0])
            direction = s[1]
            grid = []
            for j in range(n):
                 grid.append(parseline(fin.readline().rstrip('\n')))
            qin.put((i, n, direction, grid))
    return t

def solveAB2015(n, direction, grid):
    res = [[0] * n for i in range(n)]
    if direction == 'left':
        for i in range(n):
            tmp = deque()
            for j in range(n):
                if grid[i][j] != 0:
                    tmp.append(grid[i][j])
            idx = 0
            while len(tmp) > 0:
                if len(tmp) == 1 or tmp[0] != tmp[1]:
                    res[i][idx] = tmp.popleft()
                else:
                    res[i][idx] = tmp.popleft() + tmp.popleft()
                idx += 1
    elif direction == 'right':
        for i in range(n):
            tmp = deque()
            for j in range(n - 1, -1, -1):
                if grid[i][j] != 0:
                    tmp.append(grid[i][j])
            idx = n - 1
            while len(tmp) > 0:
                if len(tmp) == 1 or tmp[0] != tmp[1]:
                    res[i][idx] = tmp.popleft()
                else:
                    res[i][idx] = tmp.popleft() + tmp.popleft()
                idx -= 1
    elif direction == 'up':
        for j in range(n):
            tmp = deque()
            for i in range(n):
                if grid[i][j] != 0:
                    tmp.append(grid[i][j])
            idx = 0
            while len(tmp) > 0:
                if len(tmp) == 1 or tmp[0] != tmp[1]:
                    res[idx][j] = tmp.popleft()
                else:
                    res[idx][j] = tmp.popleft() + tmp.popleft()
                idx += 1
    else:
        for j in range(n):
            tmp = deque()
            for i in range(n - 1, -1, -1):
                if grid[i][j] != 0:
                    tmp.append(grid[i][j])
            idx = n - 1
            while len(tmp) > 0:
                if len(tmp) == 1 or tmp[0] != tmp[1]:
                    res[idx][j] = tmp.popleft()
                else:
                    res[idx][j] = tmp.popleft() + tmp.popleft()
                idx -= 1
    s = '\n'
    for i in range(n):
        s = s + ' '.join([str(v) for v in res[i]]) + '\n'
    return s.rstrip('\n')

def parseAC2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            equations = []
            for j in range(n):
                equations.append(fin.readline().rstrip('\n'))
            q = int(fin.readline().rstrip('\n'))
            queries = []
            for j in range(q):
                queries.append(fin.readline().rstrip('\n'))
            qin.put((i, n, equations, q, queries))
    return t

def solveAC2015(n, equations, q, queries):
    word = {}
    w = 0
    plus = defaultdict(dict)
    minus = defaultdict(dict)
    flag = True
    while flag:
        flag = False
        for e in equations:
            t = e.split('+')
            x = t[0]
            if x not in word:
                word[x] = w
                w += 1
            t = t[1].split('=')
            y = t[0]
            if y not in word:
                word[y] = w
                w += 1
            z = int(t[1])
            x, y = word[x], word[y]
            plus[x][y] = z
            plus[y][x] = z
            for t in minus[y]:
                if t not in plus[x]:
                    plus[x][t] = plus[x][y] - minus[y][t]
                    plus[t][x] = plus[x][t]
                    flag = True
            for t in minus[x]:
                if t not in plus[y]:
                    plus[y][t] = plus[y][x] - minus[x][t]
                    plus[t][y] = plus[y][t]
                    flag = True
            for t in plus[y]:
                if t not in minus[x]:
                    minus[x][t] = plus[x][y] - plus[y][t]
                    minus[t][x] = -minus[x][t]
                    flag = True
            for t in plus[x]:
                if t not in minus[y]:
                    minus[y][t] = plus[y][x] - plus[x][t]
                    minus[t][y] = -minus[y][t]
                    flag = True
    res = ''
    for q in queries:
        t = q.split('+')
        x, y = t[0], t[1]
        if x not in word or y not in word:
            continue
        x, y = word[x], word[y]
        if y in plus[x]:
            res += q + '=' + str(plus[x][y]) + '\n'
    return res.rstrip('\n')

def parseAD2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            v = parseline(fin.readline().rstrip('\n'))
            n, m, s = v[0], v[1], v[2:]
            qin.put((i, n, m, s))
    return t

def solveAD2015(n, m, s):
    res = 0
    s = [2 ** v for v in s]
    s.sort(reverse=True)
    t = SortedList()
    for i in range(n):
        idx = bisect.bisect_left(t, (s[i], s[i]))
        if idx >= len(t):
            res += 1
            if s[i] < m:
                t.add((m - s[i], m))
                t.add((min(s[i], m - s[i]), max(s[i], m - s[i])))
        else:
            short_edge, long_edge = t[idx]
            if long_edge == s[i]:
                del t[idx]
            else:
                del t[idx]
                if short_edge == s[i]:
                    t.add((min(short_edge, long_edge - s[i]), max(short_edge, long_edge - s[i])))
                else:
                    t.add((min(short_edge, long_edge - s[i]), max(short_edge, long_edge - s[i])))
                    t.add((min(s[i], short_edge - s[i]), max(s[i], short_edge - s[i])))
    return res