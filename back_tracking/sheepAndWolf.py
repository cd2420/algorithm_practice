# 프로그래머스
# 양과 늑대
def dfs(graph, info, pathes, now, sheep_wolf):
    global answer
    sheep_wolf[now] += 1
    if sheep_wolf[1] == sheep_wolf[0]:
        return sheep_wolf[0]

    for path in pathes:
        for nxt in graph[path]:
            if nxt in pathes:
                continue
            pathes.append(nxt)
            result = dfs(graph, info, pathes, info[nxt], sheep_wolf)
            answer = max(result, answer)
            pathes.pop()
            sheep_wolf[info[nxt]] -= 1
            
    return sheep_wolf[0]
        

def solution(info, edges):
    global answer
    answer = 0
    graph = [[] for _ in range(len(info))]
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    dfs(graph, info, [0], 0, [0, 0])
    return answer