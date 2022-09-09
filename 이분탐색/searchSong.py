# 프로그래머스
# 가사 검색
from bisect import bisect_left, bisect_right
from collections import defaultdict
def find_song(arr, a, z):
    return bisect_right(arr, z) - bisect_left(arr, a)

def solution(words, queries):
    answer = []
    wordList = defaultdict(list)
    wordListRevers = defaultdict(list)
    for word in words:
        wordList[len(word)].append(word)
        wordListRevers[len(word)].append(word[::-1])
        
    for key in wordList:
        wordList[key].sort()
        wordListRevers[key].sort()
    
    for query in queries:
        
        cnt = 0
        a_replace_word = query.replace("?", "a")
        z_replace_word = query.replace("?", "z")
        if query[0] != "?":
            cnt = find_song(wordList[len(query)], a_replace_word, z_replace_word)
        else :
            cnt = find_song(wordListRevers[len(query)], a_replace_word[::-1], z_replace_word[::-1])
        answer.append(cnt)
        
    return answer