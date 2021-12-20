# 무한 수열
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)


def get(n, p, q):
    if n <= 0:
        return 1
    if n not in A:
        A[n] = get(n // p, p, q) + get(n // q, p, q)
    return A[n]


A = defaultdict(int)
A[0] = 1
n, p, q = map(int, input().split())
result = get(n, p, q)
print(result)
