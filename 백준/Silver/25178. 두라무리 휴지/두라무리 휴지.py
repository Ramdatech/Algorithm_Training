n = int(input())
(a1, *a2, a3), (b1, *b2, b3) = [(input()) for _ in range(2)]
msk = 'aeiou'
if all([sorted(a2) == sorted(b2), a1 == b1, a3 == b3]) :
    a2 = [s for s in a2 if s not in msk]
    b2 = [s for s in b2 if s not in msk]
    if a2 == b2 :
        print("YES")
    else : 
        print("NO")
else : 
    print("NO")