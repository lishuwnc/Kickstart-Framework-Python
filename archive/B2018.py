from utility import *

def parseBA2018(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            f, l = parseline(fin.readline().rstrip('\n'))
            qin.put((i, f, l))
    return t

def solveBA2018(f, l):
    def helper(n):
        t = n // 10 * 10
        ret = 0
        p = 1
        while t > 0:
            ret += p * (t % 10)
            t //= 10
            p *= 9
        ret = ret // 9 * 8
        for t in range(n // 10 * 10, n + 1):
            if '9' not in str(t) and t % 9 != 0:
                ret += 1
        return ret
    return helper(l) - helper(f - 1)

def parseBB2018(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, k, p = parseline(fin.readline().rstrip('\n'))
            constraints = []
            for j in range(k):
                constraints.append(parseline(fin.readline().rstrip('\n')))
            qin.put((i, n, k, p, constraints))
    return t

def solveBB2018(n, k, p, constraints):
    count = [[0] * (2 ** 15) for _ in range(n + 1)]
    for i in range(2 ** 15):
        count[n][i] = 1
    for i in range(n - 1, -1, -1):
        for j in range(2 ** 15):
            for x in range(2):
                f = True
                for a, b, c in constraints:
                    if b - 1 != i:
                        continue
                    y = sum([1 for _c in bin(j % (1 << (b - a))) if _c == '1'])
                    if y + x != c:
                        f = False
                        break

                if f:
                    count[i][j] += count[i + 1][(j & 0x3fff) * 2 + x]
                else:
                    count[i + 1][(j & 0x3fff) * 2 + x] = 0
            if count[i][j] > p:
                count[i][j] = p
    res = ''
    idx = 1
    t = 0
    while idx <= n:
        t &= 0x3fff
        t *= 2
        if count[idx][t] >= p:
            res += '0'
        else:
            res += '1'
            p -= count[idx][t]
            t += 1
        idx += 1
    return res