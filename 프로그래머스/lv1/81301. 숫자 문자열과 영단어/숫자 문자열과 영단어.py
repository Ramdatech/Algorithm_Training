def solution(s):
    li = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx, x in enumerate(li) :
        s = s.replace(x, str(idx))
    return int(s)