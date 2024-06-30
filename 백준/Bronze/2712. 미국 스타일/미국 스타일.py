n = int(input())

swap = {
    "kg": "lb",
    "lb": "kg",
    "l": "g",
    "g": "l"
}

def prt(num) :
    tmp = round(num, 4)
    print(f"{tmp:.4f}", end=" ")

for _ in range(n) :
    a, b = input().split()
    a = float(a)
    if b == "kg" :
        prt(a*2.2046)
    elif b == "lb" :
        prt(a*0.4536)
    elif b == "l" :
        prt(a*0.2642)
    elif b == "g" :
        prt(a*3.7854)
    print(swap[b])