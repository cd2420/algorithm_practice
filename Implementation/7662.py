# 이중 우선순위 큐
import sys
import heapq

input = sys.stdin.readline
for _ in range(int(input())):
    k = int(input())
    visited = [False] * k
    min_q = []
    max_q = []
    for i in range(k):
        a, b = input().split()
        n_b = int(b)
        if a == 'I':
            heapq.heappush(min_q, (n_b, n_b, i))
            heapq.heappush(max_q, (n_b*-1, n_b, i))
        else :
            if min_q and max_q:
                if n_b == 1:
                    while max_q:
                        n, r_n, idx = heapq.heappop(max_q)
                        if visited[idx]:
                            continue
                        else :
                            visited[idx] = True
                            break
                else :
                    while min_q:
                        n, r_n, idx = heapq.heappop(min_q)
                        if visited[idx]:
                            continue
                        else :
                            visited[idx] = True
                            break

    max_n = 1e9
    min_n = -1e9
    while max_q:
        n, r_n, idx = heapq.heappop(max_q)
        if visited[idx]:
            continue
        else :
            max_n = r_n
            break
    while min_q:
        n, r_n, idx = heapq.heappop(min_q)
        if visited[idx]:
            continue
        else :
            min_n = r_n
            break
    if max_n == 1e9 or min_n == -1e9:
        print('EMPTY')
    else:
        print(max_n, min_n)
            