

def solution(lines):
    answer = set()
    for i in range(len(lines)):
        listy = lines[i:] + lines[:i]
        lim_1 = set([f'{x}={x+1}' for x in range(listy[0][0], listy[0][1])])
        lim_1 &= set([f'{x}={x+1}' for x in range(listy[1][0], listy[1][1])])
        answer |= lim_1

    return len(answer)