# 트리


class Node:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None
        self.state = 1


def dfs(node):
    global result
    if node.state == -1:
        return
    elif not node.child:
        result += 1
        return

    check_cnt = 0
    for child in node.child:
        if child.state != -1:
            dfs(child)
        else:
            check_cnt += 1
    if check_cnt == len(node.child):
        result += 1


n = int(input())
tree_root_lst = list(map(int, input().split()))
tree = {}
remove_tree = int(input())
start_node_idx = []

for i in range(n):
    tree[i] = Node(i)

for idx in range(n):
    parent_idx = tree_root_lst[idx]
    if parent_idx == -1:
        start_node_idx.append(idx)
    else:
        tree[idx].parent = tree[parent_idx]
        tree[parent_idx].child.append(tree[idx])
tree[remove_tree].state = -1
result = 0
for start in start_node_idx:
    dfs(tree[start])
print(result)
