def solution(absolutes, signs):
    return sum([a if s==True else -a  for s, a in zip(signs, absolutes)] )