# 프로그래머스
# 표 편집
from collections import deque
class Node:
    def __init__(self, data):
        self.status = 'O'
        self.data = data
        self.left = None
        self.right = None

def solution(n, k, cmd):
    answer = ''
    nodes = {}
    for i in range(n):
        nodes[i] = Node(i)
    nodes[0].right = nodes[1]
    nodes[n-1].left = nodes[n-2]
    for i in range(1, n-1):
        nodes[i].left = nodes[i-1]
        nodes[i].right = nodes[i+1]
    
    deleted = []
    node = nodes[k]
    cmd = deque(cmd)
    while cmd:
        func = cmd.popleft().split()
        if func[0] == 'Z':
            idx = deleted.pop()
            restore_node = nodes[idx]
            restore_node.status = 'O'
            left_node = restore_node.left
            right_node = restore_node.right
            
            if left_node:
                restore_node.right = left_node.right
                left_node.right = restore_node
            
            if right_node:
                restore_node.left = right_node.left
                right_node.left = restore_node
        elif func[0] == 'C':
            node.status = 'X'
            deleted.append(node.data)
            left = node.left
            right = node.right
            if left:
                left.right = node.right
            if right:
                right.left = node.left
                node = right
            else :
                node = left
        else:
            cnt = int(func[1])
            if func[0] == 'D':
                for _ in range(cnt):
                    node = node.right
            else :
                for _ in range(cnt):
                    node = node.left
    for n in nodes:
        answer += nodes[n].status
    return answer