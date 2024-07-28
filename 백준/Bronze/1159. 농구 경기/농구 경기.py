n = int(input())
arr = [0]*26
for _ in range(n):
    arr[ord(input()[0])-97] += 1
if max(arr) < 5:
    print("PREDAJA")
else :
    for i in range(26):
        if arr[i] >= 5:
            print(chr(i+97), end='')
