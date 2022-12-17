def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0 :
        return len(cities) * 5
    for city in cities : 
        city = city.lower()
        if city not in cache :
            cache.append(city)
            cache = cache[-cacheSize:]
            answer += 5
        else :
            cache.remove(city)
            cache.append(city)
            answer += 1
            
    return answer