from sortedcontainers import SortedList, SortedDict
from collections import Counter, defaultdict, deque
import bisect
import heapq
from functools import total_ordering
import fractions
import math
import numpy as np

class UnionSet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.p = self

    def getRoot(self):
        if self.p is not self:
            self.p = self.p.getRoot()
        return self.p

    def merge(self, other):
        if self.getRoot() is other.getRoot():
            return False
        else:
            other.p.p = self.p
            return True

class TrieNode:
    def __init__(self, c, isWord=False):
        self.c = c
        self.isWord = isWord
        self.pointers = {}

def fastPow(base, power, divisor):
    if power <= 1:
        return (base ** power) % divisor
    ret = (fastPow(base, power // 2, divisor) ** 2) % divisor
    if power % 2 == 1:
        ret = ret * base % divisor
    return ret

def fastPowMat(mat, power):
    if power == 1:
        return mat
    ret = fastPowMat(mat, power // 2)
    ret = np.dot(ret, ret)
    if power % 2 == 1:
        ret = np.dot(ret, mat)
    return ret


def parseline(line, dtype_fn=int, delimiter=' '):
    return [dtype_fn(v) for v in line.split(delimiter)]

def nCr(n, r, divisor):
    r = min(r, n - r)
    t1 = 1
    for i in range(1, r + 1):
        t1 *= i
    t2 = 1
    for i in range(n, n - r, -1):
        t2 *= i
    return t2 // t1 % divisor

def factorial(n, divisior):
    if n == 0:
        return 1 % divisior
    ret = 1
    for i in range(1, n + 1):
        ret = (ret * i) % divisior
    return ret

def isCircleCross(a, ra, b, rb, c, rc):
    def dis(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

    if dis(a, b) > (ra + rb) ** 2:
        return False
    if dis(a, c) > (ra + rc) ** 2:
        return False
    if dis(b, c) > (rb + rc) ** 2:
        return False
    if dis(a, b) < (ra - rb) ** 2:
        return True
    if dis(a, c) < (ra - rc) ** 2:
        return True
    if dis(b, c) < (rb - rc) ** 2:
        return True

    return False