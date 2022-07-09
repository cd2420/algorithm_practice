# 프로그래머스
# 여행경로
from collections import defaultdict

def dfs(start, tree, lst):
    now = tree[start]

    if not now:
        if check(tree):
            return lst
        else :
            return
        
    for i in range(len(now)):
        nxt = now.pop(i)
        lst.append(nxt)
        data = dfs(nxt, tree, lst)
        if data:
            return data
        lst.pop()    
        now.insert(i, nxt)
        
def check(tree):
    for t in tree:
        if tree[t]:
            return False
    return True

def solution(tickets):

    tree = defaultdict(list)
    for a,b in tickets:
        tree[a].append(b)
        tree[a].sort()
    answer = ["ICN"]
    dfs("ICN", tree, answer)
    return answer