# 곱하기 혹은 더하기

def dfs(func):
    if len(func) == check - 1:
        tmp_func.append(func[:])
        return
    
    func.append('+')
    dfs(func)
    func.pop()

    func.append('*')
    dfs(func)
    func.pop()

arr = list(input())
check = len(arr)
tmp_func = []
dfs([])
result = -1
for func in tmp_func:
    string = ''
    str_length = len(func)
    for i in range(str_length):
        string += arr[i] + func[i]
    string += arr[-1]
    result = max(result, eval(string))
print(result)