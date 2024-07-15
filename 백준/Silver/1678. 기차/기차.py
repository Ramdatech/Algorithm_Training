(T,M,N),l,a,b=map(int, input().split()),[],1e9,[0,0]
for _ in range(T):
    tn, *ts, _ = input().split()
    for t in map(int, ts):
        l+=[[t,tn]]
        for dt in [0,60]:
            S=t+dt-M
            if 0<=S<a : a,b=S,l[-1]
l.sort()
print(l[(l.index(b)+N)%len(l)-1][1])