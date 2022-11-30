import sys
input = sys.stdin.readline
n, m = map(int,input().strip().split())
score = [0, 0]
exp = 1
while n//(5**exp) or n//(2**exp):
    score[0] += n//(5**exp)
    score[0] -= (n-m)//(5**exp)
    score[0] -= m//(5**exp)
    score[1] += n//(2**exp)
    score[1] -= (n-m)//(2**exp)
    score[1] -= m//(2**exp)
    exp += 1

print(min(score))