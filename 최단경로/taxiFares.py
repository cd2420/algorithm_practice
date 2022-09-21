# 프로그래머스
# 합승 택시 요금
import heapq

def dkstra(start, n, fareGraph):
    
    distance = [1e9] * (n+1)
    distance[start] = 0
    q = [(0, start)]
    
    while q:
        cnt, now = heapq.heappop(q)
        if distance[now] < cnt:
            continue
        
        for i in fareGraph[now]:
            nxt = i[0]
            dist = i[1]
            if distance[nxt] > cnt + dist:
                distance[nxt] = cnt + dist
                heapq.heappush(q, (distance[nxt], nxt))
    return distance
        
def solution(n, s, a, b, fares):
    answer = 1e9
    graph = [[-1] * (n+1)]
    fareGraph = [[] for _ in range(n+1)]
    for c,d,f in fares:
        fareGraph[c].append((d, f))
        fareGraph[d].append((c, f))
    for i in range(1, n+1):
        graph.append(dkstra(i, n, fareGraph))
    
    for i in range(1, n+1):
        cnt = graph[s][i] + graph[i][a] + graph[i][b]
        answer = min(answer, cnt)
    
    return answer