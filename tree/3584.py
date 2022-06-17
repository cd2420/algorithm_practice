# 가장 가까운 공통 조상 (다시)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def count_level(x, tree, level, count):
    if level[x] != -1:
        return
    level[x] = count
    for i in tree[x]:
        if level[i] == -1:
            count_level(i, tree, level, count + 1)
result = []
for _ in range(int(input())):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    isHaveParent = [False] * (n + 1)
    for __ in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
        isHaveParent[b] = True
    level = [-1] * (n+1)
    root = 0
    for i in range(1, n+1):
        if not isHaveParent[i]:
            root = i
            break

    count_level(root, tree, level, 0)
    x, y = map(int, input().split())
    
    while level[x] != level[y]:

        if level[x] > level[y]:
            for i in tree[x]:
                if level[x] > level[i]:
                    x = i
                    break
        elif level[x] < level[y]:
            for i in tree[y]:
                if level[y] > level[i]:
                    y = i
                    break
    while x != y :
        for i in tree[x]:
            if level[x] > level[i]:
                x = i
                break
        for i in tree[y]:
            if level[y] > level[i]:
                y = i
                break
        
    result.append(x)
for r in result:
    print(r)