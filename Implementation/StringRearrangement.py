# 문자열 재정렬
nums = [str(i) for i in range(1, 10)]
string = input()
onlyStr = []
onlyNum = []
for i in range(len(string)):
    if string[i] in nums:
        onlyNum.append(int(string[i]))
    else :
        onlyStr.append(string[i])
onlyStr.sort()
totalNum = sum(onlyNum)
result = ''.join(onlyStr) + str(totalNum)
print(result)