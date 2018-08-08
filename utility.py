from sortedcontainers import SortedList, SortedDict
from collections import Counter, defaultdict, deque
import bisect
import heapq
from functools import total_ordering
import fractions
import math

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

def fastPow(base, power, divisor=10**9 + 7):
    if power <= 1:
        return base ** power
    ret = (fastPow(base, power // 2) ** 2) % divisor
    if power % 2 == 1:
        ret = ret * base % divisor
    return ret

def parseline(line, dtype_fn=int, delimiter=' '):
    return [dtype_fn(v) for v in line.split(delimiter)]

def nCr(n, r, divisor=10 ** 9 + 7):
    r = min(r, n - r)
    t1 = 1
    for i in range(1, r + 1):
        t1 *= i
    t2 = 1
    for i in range(n, n - r, -1):
        t2 *= i
    return t2 // t1 % divisor