def solution(sides):
    sides.sort()
    return len(set([x for x in range(sides[1],sum(sides))] + [x for x in range(sides[1]-sides[0]+1, sides[1])]))