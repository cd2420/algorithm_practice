# LCA
import sys
sys.setrecursionlimit(100000)
def checkDepth(x, cnt):
    if depth[x] != -1:
        return
    depth[x] = cnt
    for i in node[x]:
        if depth[i] != -1:
            continue
        parent_node[i] = x
        checkDepth(i, cnt + 1)

def find_parent_node(a, b):

    while depth[a] != depth[b]:
        
        if depth[a] > depth[b]:
            a = parent_node[a]
        else :
            b = parent_node[b]
        
    
    while a != b:
        a = parent_node[a]
        b = parent_node[b]

    return a

n = int(input())
node = [[] for _ in range(n+1)]
parent_node = [-1] * (n+1)
depth = [-1] * (n+1)
for _ in range(n-1):
    a,b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
checkDepth(1, 0)

m = int(input())
result = []
for _ in range(m):
    a,b = map(int, input().split())
    result.append(find_parent_node(a, b))

for r in result:
    print(r)