from utility import *

def parseDA2018(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            N, O, D = parseline(fin.readline().rstrip('\n'))
            X1, X2, A, B, C, M, L = parseline(fin.readline().rstrip('\n'))
            qin.put((i, N, O, D, X1, X2, A, B, C, M, L))
    return t

def solveDA2018(N, O, D, X1, X2, A, B, C, M, L):
    X = [X1, X2]
    for i in range(2, N):
        X.append((A * X[-1] + B * X[-2] + C) % M)
    sweet = [x + L for x in X]
    if O == 0 and not any([s % 2 == 0 for s in sweet]):
        print('IMPOSSIBLE')
        return 'IMPOSSIBLE'
    res = min(sweet)
    if res > D:
        print('IMPOSSIBLE')
        return 'IMPOSSIBLE'
    sweet = [0] + sweet
    odd_count = [0]
    for i in range(N):
        if sweet[i + 1] % 2 == 1:
            odd_count.append(odd_count[-1] + 1)
        else:
            odd_count.append(odd_count[-1])
        sweet[i + 1] += sweet[i]
    for i in range(1, N + 1):
        for j in range(i - 1, -1, -1):
            if odd_count[i] - odd_count[j] > O:
                break
            if sweet[i] - sweet[j] <= D:
                res = max(res, sweet[i] - sweet[j])
    print(res)
    return res

def parseDB2018(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            N, K = parseline(fin.readline().rstrip('\n'))
            argsP = parseline(fin.readline().rstrip('\n'))
            argsH = parseline(fin.readline().rstrip('\n'))
            argsX = parseline(fin.readline().rstrip('\n'))
            argsY = parseline(fin.readline().rstrip('\n'))
            qin.put((i, N, K, argsP, argsH, argsX, argsY))
    return t

def solveDB2018(N, K, argsP, argsH, argsX, argsY):
    p = [argsP[0], argsP[1]]
    h = [argsH[0], argsH[1]]
    for i in range(2, N):
        p.append((argsP[2] * p[-1] + argsP[3] * p[-2] + argsP[4]) % argsP[5] + 1)
        h.append((argsH[2] * h[-1] + argsH[3] * h[-2] + argsH[4]) % argsH[5] + 1)
    x = [argsX[0], argsX[1]]
    y = [argsY[0], argsY[1]]
    for i in range(2, K):
        x.append((argsX[2] * x[-1] + argsX[3] * x[-2] + argsX[4]) % argsX[5] + 1)
        y.append((argsY[2] * y[-1] + argsY[3] * y[-2] + argsY[4]) % argsY[5] + 1)

    # res = 0
    # for i in range(K):
    #     for j in range(N):
    #         if h[j] >= y[i] and abs(x[i] - p[j]) <= h[j] - y[i]:
    #             res += 1
    #             break
    # return res
    p, h = zip(*sorted(zip(p, h)))
    p = list(p)
    h = list(h)
    last_p, last_h = p[0], h[0]
    for i in range(1, N):
        if p[i] - last_p <= last_h - h[i]:
            h[i] = last_h - p[i] + last_p
            continue
        else:
            last_p = p[i]
            last_h = h[i]
            j = i - 1
            while j >= 0 and last_p - p[j] < last_h - h[j]:
                h[j] = last_h - last_p + p[j]
                j -= 1
    res = 0
    for i in range(K):
        idx = bisect.bisect_left(p, x[i])
        if idx == 0:
            res += 1 if y[i] <= h[idx] - p[idx] + x[i] else 0
        elif idx == N:
            res += 1 if y[i] <= h[idx - 1] - x[i] + p[idx - 1] else 0
        else:
            if y[i] <= h[idx] - p[idx] + x[i] or y[i] <= h[idx - 1] - x[i] + p[idx - 1]:
                res += 1
    return res

def parseDC2018(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            R, C, W = parseline(fin.readline().rstrip('\n'))
            grid = []
            for j in range(R):
                grid.append(fin.readline().rstrip('\n'))
            dictionary = []
            for j in range(W):
                dictionary.append(fin.readline().rstrip('\n'))
            qin.put((i, R, C, W, grid, dictionary))
    return t

def solveDC2018(R, C, W, grid, dictionary):
    root = TrieNode('@')
    for word in dictionary:
        p = root
        for c in word:
            if c not in p.pointers:
                p.pointers[c] = TrieNode(c)
            p = p.pointers[c]
        p.isWord = True
    left = [[[0] * (C + 1) for i in range(C)] for j in range(R)]
    pass_x = [[0] * (C + 1) for i in range(R + 1)]
    right = [[[0] * (C + 1) for i in range(C)] for j in range(R)]
    top = [[[0] * (R + 1) for i in range(C)] for j in range(R)]
    pass_y = [[0] * (C + 1) for i in range(R + 1)]
    bottom = [[[0] * (R + 1) for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C - 1, -1, -1):
            p = root
            sz = 1
            flag = True
            while True:
                if j + sz > C:
                    break
                if grid[i][j + sz - 1] not in p.pointers:
                    flag = False
                if flag:
                    p = p.pointers[grid[i][j + sz - 1]]
                    if p.isWord:
                        right[i][j][sz] = sz
                        for k in range(j + 1, j + sz):
                            pass_y[i + 1][k + 1] += sz
                    else:
                        right[i][j][sz] = 0
                if j != C - 1:
                    right[i][j][sz] += right[i][j + 1][sz - 1]
                sz += 1
    for i in range(R):
        for j in range(C):
            p = root
            sz = 1
            flag = True
            while True:
                if j + 1 - sz < 0:
                    break
                if grid[i][j + 1 - sz] not in p.pointers:
                    flag = False
                if flag:
                    p = p.pointers[grid[i][j + 1 - sz]]
                    if p.isWord:
                        left[i][j][sz] = sz
                        for k in range(j, j - sz + 1, -1):
                            pass_y[i + 1][k + 1] += sz
                    else:
                        left[i][j][sz] = 0
                sz += 1
    for i in range(R - 1, -1, -1):
        for j in range(C):
            p = root
            sz = 1
            flag = True
            while True:
                if i + sz > R:
                    break
                if grid[i + sz - 1][j] not in p.pointers:
                    flag = False
                if flag:
                    p = p.pointers[grid[i + sz - 1][j]]
                    if p.isWord:
                        bottom[i][j][sz] = sz
                        for k in range(i + 1, i + sz):
                            pass_x[k + 1][j + 1] += sz
                    else:
                        bottom[i][j][sz] = 0
                if i != R - 1:
                    bottom[i][j][sz] += bottom[i + 1][j][sz - 1]
                sz += 1
    for i in range(R):
        for j in range(C):
            p = root
            sz = 1
            flag = True
            while True:
                if i + 1 - sz < 0:
                    break
                if grid[i + 1 - sz][j] not in p.pointers:
                    flag = False
                if flag:
                    p = p.pointers[grid[i + 1 - sz][j]]
                    if p.isWord:
                        top[i][j][sz] = sz
                        for k in range(i, i - sz + 1, -1):
                            pass_x[k + 1][j + 1] += sz
                    else:
                        top[i][j][sz] = 0
                sz += 1
    for i in range(R):
        for j in range(C):
            pass_x[i + 1][j + 1] += pass_x[i + 1][j]
            pass_y[i + 1][j + 1] += pass_y[i][j + 1]
    # print('left', left)
    # print('right', right)
    # print('top', top)
    # print('bottom', bottom)

    max_funny = 0
    count = 0
    funny = [[0] * (C + 1) for i in range(R + 1)]
    for i in range(R):
        for j in range(C):
            funny[i + 1][j + 1] = funny[i][j + 1] + funny[i + 1][j] - funny[i][j] + top[i][j][i + 1] + left[i][j][j + 1] + right[i][0][j + 1] + bottom[0][j][i + 1]
            for k in range(1, j + 1):
                funny[i + 1][j + 1] += left[i][j][k]
            for k in range(1, i + 1):
                funny[i + 1][j + 1] += top[i][j][k]
    # print(funny)
    #print(pass_x, pass_y)
    numerator = 0
    de = 1
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            for p in range(i):
                for q in range(j):
                    #tmp = (funny[i][j] - funny[p][j] - funny[i][q] + funny[p][q] - stacked_left[i - 1][j - 1][j] + stacked_left[i - 1][j - 1][j - q] - stacked_top[i - 1][j - 1][i] + stacked_top[i - 1][j - 1][i - p]) / (i - p + j - q)
                    tmp = (funny[i][j] - funny[p][j] - funny[i][q] + funny[p][q] - pass_x[p + 1][j] + pass_x[p + 1][q] - pass_y[i][q + 1] + pass_y[p][q + 1]) / (i - p + j - q)
                    if tmp == max_funny:
                        count += 1
                    elif tmp > max_funny:
                        count = 1
                        max_funny = tmp
                        #numerator = (funny[i][j] - funny[p][j] - funny[i][q] + funny[p][q] - stacked_left[i - 1][j - 1][j] + stacked_left[i - 1][j - 1][j - q] - stacked_top[i - 1][j - 1][i] + stacked_top[i - 1][j - 1][i - p])
                        numerator = (funny[i][j] - funny[p][j] - funny[i][q] + funny[p][q] - pass_x[p + 1][j] + pass_x[p + 1][q] - pass_y[i][q + 1] + pass_y[p][q + 1])
                        de = i - p + j - q
    print(max_funny)
    max_funny = fractions.Fraction(numerator, de)
    return '{0}/{1} {2}'.format(max_funny.numerator, max_funny.denominator, count)