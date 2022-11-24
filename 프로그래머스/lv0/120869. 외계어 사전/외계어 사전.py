def solution(spell, dic):
    return 1 if sum([1 for i in dic if ''.join(sorted(spell)) in ''.join(sorted(i))]) > 0 else 2