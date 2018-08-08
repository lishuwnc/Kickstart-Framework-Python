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