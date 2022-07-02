#  숨바꼭질
import heapq

n, m = map(int, input().split())
check = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    check[a].append(b)
    check[b].append(a)

arr = [1e9] * (n + 1)
arr[1] = 0
q = []
max_dist = 0
heapq.heappush(q, (0, 1))
while q:
    cnt, x = heapq.heappop(q)
    if arr[x] < cnt:
        continue
    for nxt in check[x]:
        if arr[nxt] > cnt + 1:
            arr[nxt] = cnt + 1
            max_dist = max(max_dist, arr[nxt])
            heapq.heappush(q, (cnt+1, nxt))

first_idx = -1
cnt = 0
for i in range(1, n+1):
    if arr[i] == max_dist:
        if first_idx == -1:
            first_idx = i
        cnt += 1
        
print(first_idx, max_dist, cnt)