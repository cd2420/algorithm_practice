# APC는 왜 서브태스크 대회가 되었을까?
n, l, k = map(int, input().split())
problems = []
max_score = 0
for _ in range(n):
    easy, hard = map(int, input().split())
    if easy <= l:
        problems.append((easy, hard))
        if hard <= l:
            max_score += 1
problems.sort(key=lambda x: x[0])

result = 0
if max_score >= k:
    result = 140 * k
else:
    result = 140 * max_score
    if k - max_score <= len(problems) - max_score:
        result += 100 * (k - max_score)
    else:
        result += 100 * (len(problems) - max_score)

print(result)
