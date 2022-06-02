# 좋은 수

import sys
n = int(input())
arr = list(map(int, input().split()))
check = set()
check.add(arr[0] * 2)
result = 0
for i in range(1, n):
    for j in range(i):
        if (arr[i] - arr[j]) in check:
            result += 1
            break
    for j in range(i+1):
        check.add(arr[i]+arr[j])
print(result)