# [1차] 캐시
def solution(cacheSize, cities):
    cities = list(city.upper() for city in cities)
    cache = ["" for _ in range(cacheSize)]
    used = [1 for _ in range(cacheSize)]
    time = 0

    if cacheSize == 0: 
        return 5 * len(cities)

    for city in cities:
        if city in cache: # hit
            time += 1
            used[cache.index(city)] = 0
        else: # miss
            time += 5
            maxNum = max(used)
            maxNumI = used.index(maxNum)
            cache[maxNumI] = city
            used[maxNumI] = 0
        for j in range(cacheSize):
            used[j] += 1
        
    return time