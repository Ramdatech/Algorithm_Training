import sys 
from math import pi
input = sys.stdin.readline
n = int(input())
uc = (n**2)*pi
taxi = (n*(2**0.5))**2
print(f'{uc:.6f}')
print(f'{taxi:.6f}')