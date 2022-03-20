# 트리
import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_tree(tree, pre_idx, preorder_list, inorder_list):
    if pre_idx >= len(preorder_list):
        return
    node = preorder_list[pre_idx]
    if node in inorder_list:
        idx = inorder_list.index(node)
        if inorder_list[:idx]:
            rst = find_tree(tree, pre_idx + 1, preorder_list,
                            inorder_list[:idx])
            if rst:
                tree[node].left = tree[preorder_list[rst]]

        if inorder_list[idx+1:]:
            rst = find_tree(tree, pre_idx + 1, preorder_list,
                            inorder_list[idx+1:])
            if rst:
                tree[node].right = tree[preorder_list[rst]]
        return pre_idx
    else:
        return find_tree(tree, pre_idx + 1, preorder_list, inorder_list)


def postorder(tree, node):
    if node.left:
        postorder(tree, node.left)
    if node.right:
        postorder(tree, node.right)
    print(node.data, end=' ')


for _ in range(int(input())):
    n = int(input())
    preorder_list = list(map(int, input().split()))
    inorder_list = list(map(int, input().split()))
    tree = {}
    for i in range(1, n+1):
        tree[i] = Node(i)

    find_tree(tree, 0, preorder_list, inorder_list)
    postorder(tree, tree[preorder_list[0]])
    print()
