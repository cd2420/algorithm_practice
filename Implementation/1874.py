# 스택 수열
n = int(input())
nums = [i for i in range(n, 0, -1)]
stack = []
result = []
is_ok = True
for _ in range(n):
    check = int(input())
    while nums and nums[-1] <= check:
        stack.append(nums.pop())
        result.append('+')
    while stack:
        if stack[-1] <= check:
            result.append('-')
            if stack.pop() == check:
                break
        else:
            is_ok = False
            break
    if not is_ok:
        break
if is_ok:
    for r in result:
        print(r)
else:
    print('NO')
