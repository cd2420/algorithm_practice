# 가장 먼 노드
import heapq


def dkstra(adj, distance):

    heap = []
    distance[1] = 0
    heapq.heappush(heap, (0, 1))
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for next, edge in adj[now]:
            cost = dist + edge
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(heap, (cost, next))


def solution(n, edge):
    answer = 0
    adj = [[] for _ in range(n+1)]
    for i in edge:
        a, b = i
        adj[a].append((b, 1))
        adj[b].append((a, 1))

    distance = [1e9] * (n + 1)
    distance[0] = -1
    dkstra(adj, distance)
    max_dist = max(distance)
    for d in distance:
        if max_dist == d:
            answer += 1
    return answer
