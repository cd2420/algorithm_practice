# 단어섞기
for n in range(int(input())):

    answer = 'no'
    word1, word2, target = input().split()
    dp1 = [[''] * (len(target) + 1) for __ in range(len(word1) + 1)]
    dp2 = [[''] * (len(target) + 1) for __ in range(len(word2) + 1)]
    visited = [False] * len(target)

    for i in range(1, len(word1) + 1):
        for j in range(1, len(target) + 1):
            if word1[i-1] == target[j-1]:
                dp1[i][j] = dp1[i-1][j-1] + word1[i-1]
                visited[j - 1] = True
            else:
                tmp_word = max(dp1[i-1][j], dp1[i][j-1], key=lambda x: len(x))
                dp1[i][j] = tmp_word

    for i in range(1, len(word2) + 1):
        for j in range(1, len(target) + 1):
            if word2[i-1] == target[j-1]:
                dp2[i][j] = dp2[i-1][j-1] + word2[i-1]
                visited[j - 1] = True
            else:
                tmp_word = max(dp2[i-1][j], dp2[i][j-1], key=lambda x: len(x))
                dp2[i][j] = tmp_word
    visited = list(set(visited))
    if len(visited) == 1:
        if visited[0] and dp1[-1][-1] == word1 and dp2[-1][-1] == word2:
            answer = 'yes'
    print('Data set ' + str(n + 1) + ': ' + answer)
