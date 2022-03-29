# 수 묶기

def cal_number(arr):
    check = 0
    for i in range(0, len(arr), 2):
        if i + 1 < len(arr):
            if  arr[i] * arr[i+1] >= arr[i] + arr[i+1]:
                check += arr[i] * arr[i+1]
            else :
                check += arr[i] + arr[i+1]
        else :
            check += arr[i]
    return check

n = int(input())
numbers_over_0 = []
numbers_under_0 = []

for _ in range(n):
    number = int(input())
    if number > 0:
        numbers_over_0.append(number)
    else :
        numbers_under_0.append(number)

numbers_over_0.sort(reverse=True)
numbers_under_0.sort()

result = 0
result += cal_number(numbers_over_0)
result += cal_number(numbers_under_0)

print(result)