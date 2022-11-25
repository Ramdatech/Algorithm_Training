b = input()
li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in li:
    b = b.replace(i, "#")
print(len(b))