a = input().strip()
res = 0

ary = [0,3,3,3,3,3,4,3,4]
for i in range(1, len(ary)) :
    ary[i] = ary[i] + ary[i-1]

for i in a :
    n = ord(i)-ord("A")+1
    for i in range(len(ary)):
        if n <= ary[i] :
            res += i+2
            break

print(res)