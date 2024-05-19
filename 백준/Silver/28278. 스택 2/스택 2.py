import sys
t = sys.stdin.readline
n = int(t().strip())
st = []
for _ in range(n):
    a, *b = map(int, t().strip().split())
    if b == [] :
        if a == 2 :
            print(-1 if st == [] else st.pop())
        elif a == 3 :
            print(len(st))
        elif a == 4 :
            print(1 if st == [] else 0)
        elif a == 5 :
            print(-1 if st == [] else st[-1])
    else:
        st.append(b[0])