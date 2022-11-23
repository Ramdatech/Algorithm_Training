a = input()
a = int(a)
b = input()
b = int(b)

sample = 1

if a<0 and b>0:
    sample = 2
elif a<0 and b<0 :
    sample = 3
elif a>0 and b<0 :
    sample = 4
print(sample)
