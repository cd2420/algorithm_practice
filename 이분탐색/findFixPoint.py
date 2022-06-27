# 고정점 찾기

def find_binary(start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return find_binary(start, mid-1)
    else :
        return find_binary(mid+1, end)
n = int(input())
arr = list(map(int, input().split()))
result = find_binary(0, len(arr))
if result:
    print(result)
else:
    print(-1)