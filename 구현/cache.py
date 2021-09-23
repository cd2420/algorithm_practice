# 캐시
def solution(cacheSize, cities):
    answer = 0
    cache = []
    while cities:
        city = cities.pop(0).lower()
        if city not in cache:
            if cacheSize > 0:
                if len(cache) == cacheSize:
                    cache.pop()
                cache.insert(0, city)
            answer += 5
        else:
            if cacheSize > 0:
                cache.remove(city)
                cache.insert(0, city)
                answer += 1

    return answer
