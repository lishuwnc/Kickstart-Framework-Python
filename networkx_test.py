from utility import *

def parse2C2018(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            grid = []
            for j in range(n):
                grid.append(parseline(fin.readline().rstrip('\n')))
            qin.put((i, n, grid))
    return t

def solve2C2018(n, grid):
    res = 0
    while True:
        G = nx.Bipart
        G.add_nodes_from(range(2 * n))
        t = None
        c = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] is not None:
                    if t is None:
                        t = grid[i][j]
                    if grid[i][j] == t:
                        c += 1
                        grid[i][j] = None
                        G.add_edge(i, j + n)
        if t is None:
            break
        res += c - len(nx.maximal_matching(G))
    return res