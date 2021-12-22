# 결혼식
n = int(input())
m = int(input())
friends = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

result = set()
result.add(1)
for i in friends[1]:
    result.add(i)
    for j in friends[i]:
        result.add(j)
print(len(result) - 1)
