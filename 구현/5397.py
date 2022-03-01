# 키로거
import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    word = input().rstrip()
    left = deque()
    right = deque()
    for i in range(len(word)):
        if word[i] == '<':
            if left:
                right.appendleft(left.pop())
        elif word[i] == '>':
            if right:
                left.append(right.popleft())
        elif word[i] == '-':
            if left:
                left.pop()
        else:
            left.append(word[i])
    left.extend(right)
    print(''.join(left))
