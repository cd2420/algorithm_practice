# 이진검색트리
import sys
sys.setrecursionlimit(100000)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(start, parent, left, right):
    if parent:
        if parent.data > start.data:
            parent.left = start
        else:
            parent.right = start

    if left:
        preorder(left[0], start, divide_left(left), divide_right(left))
    if right:
        preorder(right[0], start, divide_left(right), divide_right(right))


def divide_left(graph):
    return_graph = []
    if graph:
        check = graph[0]
        for i in range(1, len(graph)):
            if check.data > graph[i].data:
                return_graph.append(graph[i])
    return return_graph


def divide_right(graph):
    return_graph = []
    if graph:
        check = graph[0]
        for i in range(1, len(graph)):
            if check.data < graph[i].data:
                return_graph.append(graph[i])
    return return_graph


def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.data)


nums = []
while True:
    try:
        n = int(input())
        nums.append(Node(n))
    except:
        break
left = divide_left(nums)
right = divide_right(nums)

preorder(nums[0], None, left, right)
postorder(nums[0])
