# 순위
def solution(n, results):
    answer = 0

    result_graph = [[0] * (n+1) for _ in range(n+1)]

    for result in results:
        a, b = result
        result_graph[a][b] = 1  # 1은 승리
        result_graph[b][a] = -1  # -1은 패배

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            for k in range(1, n+1):
                if j == k or i == k:
                    continue
                if result_graph[i][k] == 1 and result_graph[j][k] == -1:
                    result_graph[i][j] = 1
                    result_graph[j][i] = -1
                elif result_graph[i][k] == -1 and result_graph[j][k] == 1:
                    result_graph[i][j] = -1
                    result_graph[j][i] = 1

    for r in range(1, n+1):
        count = 0
        for i in range(1, n+1):
            if result_graph[r][i] != 0:
                count += 1
        if count == n-1:
            answer += 1

    return answer
