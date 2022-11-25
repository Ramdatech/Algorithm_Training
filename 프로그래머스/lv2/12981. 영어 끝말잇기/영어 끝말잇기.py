def solution(n, words):
    sample = [words[0]]
    for idx, i in enumerate(words[1:]) :
        if i not in sample and sample[-1][-1] == i[0]:
            sample.append(i)
        else :
            return [(idx+1)%n+1, (idx+1)//n+1] 
    return [0,0]