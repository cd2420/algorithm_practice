# 탑승구

def find_parent(x):
    if x == parent[x]:
        return x
    else :
        a = find_parent(parent[x])
        parent[x] = a
        return a

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

g = int(input())
p = int(input())
docking = [0]
for i in range(p):
    docking.append(int(input()))
parent = {}
for i in range(g+1):
    parent[i] = i
result = 0
for i in range(1, p+1):
    gate = docking[i]
    x = find_parent(gate)
    if x == 0:
        continue
    result += 1
    union_parent(x, x-1)
print(result)