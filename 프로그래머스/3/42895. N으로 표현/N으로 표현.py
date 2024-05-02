
def solution(N, number):
    dt = {1 : set([N])}
    if N == number :
        return 1
    for i in range(2, 9) :
        tmp = [(x, i-x) for x in dt if i-x in dt and i-x>0]
        tmp += [(x, x-i) for x in dt if x-i in dt and x-i>0]
        res = set([])
        for x, y in tmp : 
            for dx in dt[x] :
                for dy in dt[y] : 
                    res.add(dx+dy)
                    res.add(dx*dy)
                    if dy != 0 : res.add(dx//dy)
                    if dx >= dy : res.add(dx-dy)
        res.add(int(str(N)*i))
        dt[i] = res
        if number in dt[i] : 
            return i
    return -1