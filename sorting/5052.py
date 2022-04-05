# 전화번호 목록
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    numbers = [input().rstrip() for __ in range(n)]
    numbers.sort()
    for i in range(1, n):
        if numbers[i-1] == numbers[i][:len(numbers[i-1])]:
            print('NO')
            break
    else :
        print('YES')