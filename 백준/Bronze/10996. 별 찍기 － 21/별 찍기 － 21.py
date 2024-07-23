n = int(input())
t = "\n".join(["* " * ((n+1)//2), " *" * (n//2)]).strip()
for _ in range(n):
    print(t)