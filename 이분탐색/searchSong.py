# 프로그래머스
# 가사 검색
from bisect import bisect_left, bisect_right
from collections import defaultdict

def check(words, left, right):
    left_idx = bisect_left(words, left)
    right_idx = bisect_right(words, right)
    return right_idx - left_idx

def solution(words, queries):
    answer = []
    dic = defaultdict(list)
    reverse_dic = defaultdict(list)
    for word in words:
        dic[len(word)].append(word)
        reverse_dic[len(word)].append(word[::-1])
    
    for key in dic.keys():
        dic[key].sort()
        reverse_dic[key].sort()
        
    for query in queries:
        if query[0] != '?':
            answer.append(check(dic[len(query)], query.replace("?", "a"), query.replace("?", "z")))
        else :
            query = query[::-1]
            answer.append(check(reverse_dic[len(query)], query.replace("?", "a"), query.replace("?", "z")))
    
    return answer