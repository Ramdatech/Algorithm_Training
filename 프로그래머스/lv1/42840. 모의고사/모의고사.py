def solution(answers):
    answer = [0, 0, 0]
    testers = ["1 2 3 4 5".split(), '2 1 2 3 2 4 2 5'.split(), '3 3 1 1 2 2 4 4 5 5'.split()]
    for m, tester in enumerate(testers) :
        for idx,ans in enumerate(answers):
            if tester[idx%len(tester)] == str(ans) :
                answer[m] += 1
    
    result = []
    for idx, i in enumerate(answer):
        if i == max(answer) :
            result.append(idx+1)
            
    return result