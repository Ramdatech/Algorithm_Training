def f(a) : return a//4, a%4
print(sum(sum(sum((abs(x-y) for x, y in zip([i,j],f(ord(c)-65)))) for j, c in enumerate(input()) if c != ".") for i in range(4)))