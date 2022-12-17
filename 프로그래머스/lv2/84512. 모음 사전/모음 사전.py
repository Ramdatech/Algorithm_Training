def dfs(str, list):
    dt = set()
    if len(str) == 5 :
        return dt
    for i in list :
        text = str+i
        dt.add(text)
        dt |= dfs(text, list)
    return dt

def solution(word):
    dt = dfs("", ['A', 'E', 'I', 'O', 'U'])
    return sorted(list(dt)).index(word)+1