from utility import *

def parseCA2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            s = fin.readline().rstrip('\n')
            qin.put((i, s))
    return t

def solveCA2017(s):
    if len(s) % 2 == 1:
        return 'AMBIGUOUS'
    if len(s) == 2:
        return s[1] + s[0]
    forward = [s[0]]
    idx = 2
    while idx < len(s):
        forward.append(chr((ord(s[idx]) - ord(forward[-1])) % 26 + ord('A')))
        idx += 2
    backward = [s[-1]]
    idx = len(s) - 3
    while idx >= 0:
        backward.append(chr((ord(s[idx]) - ord(backward[-1])) % 26 + ord('A')))
        idx -= 2
    res = [None] * len(s)
    res[1::2] = forward
    res[-2::-2] = backward
    return ''.join(res)

def parseCB2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n = int(fin.readline().rstrip('\n'))
            grid = []
            for j in range(n):
                grid.append(fin.readline().rstrip('\n'))
            qin.put((i, n, grid))
    return t

def solveCB2017(n, grid):
    row_state = defaultdict(int)
    col_state = defaultdict(int)
    for i in range(n):
        t = []
        for j in range(n):
            if grid[i][j] == 'X':
                t.append(j)
        if len(t) > 2 or len(t) == 0:
            return 'IMPOSSIBLE'
        if len(t) == 1:
            t.append(0)
        row_state[(t[0], t[1])] += 1
        if row_state[(t[0], t[1])] > 2:
            return 'IMPOSSIBLE'
    if len(row_state) != n // 2 + 1:
        return 'IMPOSSIBLE'
    for i in range(n):
        t = []
        for j in range(n):
            if grid[j][i] == 'X':
                t.append(j)
        if len(t) > 2 or len(t) == 0:
            return 'IMPOSSIBLE'
        if len(t) == 1:
            t.append(0)
        col_state[(t[0], t[1])] += 1
        if col_state[(t[0], t[1])] > 2:
            return 'IMPOSSIBLE'
    if len(col_state) != n // 2 + 1:
        return 'IMPOSSIBLE'
    return 'POSSIBLE'

def parseCC2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            n, q = parseline(fin.readline().rstrip('\n'))
            answers = []
            for j in range(n + 1):
                answers.append(fin.readline().rstrip('\n'))
            scores = parseline(fin.readline().rstrip('\n'))
            qin.put((i, n, q, answers, scores))
    return t

def solveCC2017(n, q, answers, scores):
    if n == 1:
        same, diff = 0, 0
        for i in range(q):
            if answers[0][i] == answers[1][i]:
                same += 1
            else:
                diff += 1
        score = scores[0]
        return min(same, score) + diff - max(0, score - same)
    else:
        a, b, c, d = 0, 0, 0, 0
        for i in range(q):
            if answers[0][i] == answers[1][i]:
                if answers[0][i] == answers[2][i]:
                    a += 1
                else:
                    d += 1
            else:
                if answers[0][i] == answers[2][i]:
                    b += 1
                else:
                    c += 1
        res = 0
        for x1 in range(a + 1):
            for x2 in range(b + 1):
                for x3 in range(c + 1):
                    for x4 in range(d + 1):
                        if x1 + x2 + c - x3 + d - x4 == scores[0] and x1 + b - x2 + x3 + d - x4 == scores[1]:
                            res = max(res, x1 + x2 + x3 + x4)
        return res

def parseCD2017(input_file, qin):
    with open(input_file, 'r') as fin:
        t = int(fin.readline().rstrip('\n'))
        for i in range(t):
            minimum, maximum, mean, median = parseline(fin.readline().rstrip('\n'))
            qin.put((i, minimum, maximum, mean, median))
    return t

def solveCD2017(minimum, maximum, mean, median):
    if minimum > maximum or mean < minimum or mean > maximum or median < minimum or median > maximum:
        return 'IMPOSSIBLE'
    if minimum == maximum:
        return 1
    if 2 * mean == (minimum + maximum) and mean == median:
        return 2
    res = 2 ** 31
    try:
        offset = maximum + minimum + median - 3 * mean
        if offset > 0:
            if 2 * mean - minimum - median <= 0:
                raise Exception
            res = min(res, (offset + 2 * mean - minimum - median - 1) // (2 * mean - minimum - median) * 2 + 3)
        else:
            if 2 * mean - maximum - median >= 0:
                raise Exception
            res = min(res, (-offset + maximum + median - 2 * mean - 1) // (maximum + median - 2 * mean) * 2 + 3)
    except:
        pass
    try:
        offset = maximum + minimum + 2 * median - 4 * mean
        if offset > 0:
            if 2 * mean - minimum - median <= 0:
                raise Exception
            res = min(res, (offset + 2 * mean - minimum - median - 1) // (2 * mean - minimum - median) * 2 + 4)
        else:
            if 2 * mean - maximum - median >= 0:
                raise Exception
            res = min(res, (-offset + maximum + median - 2 * mean - 1) // (maximum + median - 2 * mean) * 2 + 4)
    except:
        pass
    return res if res < 2 ** 31 else 'IMPOSSIBLE'