def f(a, i, j) : return abs(a//4-i)+abs(a%4-j)
print(sum(sum(f(ord(c)-65,i,j) for j, c in enumerate(input()) if c != ".") for i in range(4)))