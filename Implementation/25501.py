# 재귀
def recursion(s, l, r, c):
    if l >= r: return [1, c]
    elif s[l] != s[r]: return [0, c]
    else: return recursion(s, l+1, r-1, c + 1)

def isPalindrome(s):
    count = 1
    return recursion(s, 0, len(s)-1, count)

n = int(input())
for i in range(n):
    word = input()
    result, check = isPalindrome(word)
    print(result, end=" ")
    print(check)