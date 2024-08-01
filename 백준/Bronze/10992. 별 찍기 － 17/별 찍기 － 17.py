t = int(input())
for i in range(1, t):
    print(f"{(t-i)*' '}*{(2*i-3)*' '}{'*' if 2*i-3 > 0 else ''}")
print((2*t-1)*"*")