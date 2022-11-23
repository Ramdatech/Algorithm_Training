a = input()
var1, var2 = a.split()
var1 = int(var1)
var2 = int(var2)

if var2 < 45 :
    var2 = var2 + 60 - 45
    var1 -= 1
else :
    var2 = var2 - 45
if var1 == -1:
    var1 = 23

print("{} {}".format(var1, var2))