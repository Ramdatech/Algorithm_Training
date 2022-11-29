def solution(s):
    answer = []
    s = [[y.strip() for y in x.split(",")] for x in s[2:-2].split("},{")]
    s = sum(sorted(s, key=lambda x: len(x)), [])
    res = set()
    for i in s :
        a = int(i)
        if set(res) & set([a]) == set() :
            answer.append(a)
            res.add(a)
            
    return list(answer)