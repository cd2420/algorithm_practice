# 프로그래머스
# 길 찾기 게임
import sys
sys.setrecursionlimit(1000000)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check(tree, root_node, nodeinfo):
    if not nodeinfo:
        return

    left_node = []
    right_node = []
    for child_node in nodeinfo:
        if child_node[2] == root_node[2]:
            continue
        if child_node[0] < root_node[0]:
            left_node.append(child_node)
        if child_node[0] > root_node[0]:
            right_node.append(child_node)
    
    if left_node:
        nxt_root_node = max(left_node, key = lambda x:x[1])
        tree[root_node[2]].left = tree[nxt_root_node[2]]
        check(tree, nxt_root_node, left_node)
    if right_node:
        nxt_root_node = max(right_node, key = lambda x:x[1])
        tree[root_node[2]].right = tree[nxt_root_node[2]]
        check(tree, nxt_root_node, right_node)

def preorder(tree, data, pre_list):
    pre_list.append(data)
    node = tree[data]
    if node.left:
        preorder(tree, node.left.data, pre_list)
    if node.right:
        preorder(tree, node.right.data, pre_list)

def postorder(tree, data, post_list):
    node = tree[data]
    if node.left:
        postorder(tree, node.left.data, post_list)
    if node.right:
        postorder(tree, node.right.data, post_list)
    post_list.append(data)

def solution(nodeinfo):
    answer = []
    tree = {}        
    tmp_node = []
    for i in range(len(nodeinfo)):
        x,y = nodeinfo[i]
        tmp_node.append([x,y,i+1])
        tree[i+1] = Node(i+1)
    
    root_node = max(tmp_node, key = lambda x:x[1])
    check(tree, root_node, tmp_node)
    
    pre_list = []
    preorder(tree, root_node[2], pre_list)
    answer.append(pre_list)
    
    post_list = []
    postorder(tree, root_node[2], post_list)
    answer.append(post_list)

    return answer