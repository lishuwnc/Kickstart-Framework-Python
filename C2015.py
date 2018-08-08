from utility import *

def parseCA2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            grid = []
            for j in range(n):
                grid.append(list(fin.readline().rstrip('\n')))
            qin.put((i, n, grid))
    return t

def solveCA2015(n, grid):
    res = 0
    delta = [-1, 0, 1, 0, -1, 1, 1, -1, -1]
    for x in range(n):
        for y in range(n):
            if grid[x][y] == '*':
                continue
            grid[x][y] = 0
            for d in range(8):
                dx, dy = delta[d], delta[d + 1]
                if x + dx >= 0 and x + dx < n and y + dy >= 0 and y + dy < n:
                    grid[x][y] += 1 if grid[x + dx][y + dy] == '*' else 0
    for x in range(n):
        for y in range(n):
            if grid[x][y] != 0:
                continue
            res += 1
            grid[x][y] = '.'
            q = deque()
            q.append((x, y))
            qsize = 1
            while qsize > 0:
                i, j = q.popleft()
                qsize -= 1
                for d in range(8):
                    dx, dy = delta[d], delta[d + 1]
                    if i + dx >= 0 and i + dx < n and j + dy >= 0 and j + dy < n:
                        if isinstance(grid[i + dx][j + dy], str):
                            continue
                        if grid[i + dx][j + dy] == 0:
                            q.append((i + dx, j + dy))
                            qsize += 1
                        grid[i + dx][j + dy] = '.'
    for x in range(n):
        for y in range(n):
            if isinstance(grid[x][y], int):
                res += 1
    return res

def parseCB2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            grid = []
            for j in range(n):
                grid.append(list(fin.readline().rstrip('\n')))
            qin.put((i, n, grid))
    return t

def parseCC2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            v = parseline(fin.readline().rstrip('\n'))
            x = int(fin.readline().rstrip('\n'))
            qin.put((i, v, x))
    return t

def solveCC2015(v, x):
    m = {}
    def helper(v, x):
        if x in m:
            return m[x]
        res = 0
        _x = x
        while x > 0:
            if v[x % 10] == 1:
                x //= 10
                res += 1
            else:
                break
        if x == 0:
            m[_x] = res
            return res
        res = 2 ** 31
        for i in range(2, _x):
            if _x % i != 0:
                continue
            res = min(res, helper(v, i) + helper(v, _x // i) + 1)
        m[_x] = res
        return res
    res = helper(v, x)
    return res + 1 if res < 2 ** 31 else 'Impossible'

def parseCD2015(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            grid = []
            for j in range(n):
                grid.append(list(fin.readline().rstrip('\n')))
            qin.put((i, n, grid))
    return t