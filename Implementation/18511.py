# 재귀
def makeNum(nums, arr, size, check):
    if len(nums) == size:
        check.add(int(nums))
        return 
    
    nums += arr[0]
    makeNum(nums, arr, size, check)
    nums = nums[:-1]

    if K >= 2:
        nums += arr[1]
        makeNum(nums, arr, size, check)
        nums = nums[:-1]
    
    if K >= 3:
        nums += arr[2]
        makeNum(nums, arr, size, check)
        nums = nums[:-1]

N, K = map(int, input().split())
arr = list(input().split())
size = len(str(N))

while True:

    check = set()
    answer = []
    makeNum("", arr, size, check)
    result = list(check)

    for r in result:
        if r <= N:
            answer.append(r)
    
    if len(answer) >= 1:
        print(max(answer))
        break
    else :
        size -= 1