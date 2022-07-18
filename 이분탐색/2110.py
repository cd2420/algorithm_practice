# 공유기 설치
n,c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
start = 1
end = arr[-1] - arr[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    now = arr[0]
    for i in range(1, n):
        if now + mid <= arr[i]:
            cnt += 1
            now = arr[i]
    if cnt >= c:
        result = mid
        start = mid + 1
    else :
        end = mid - 1
print(result)