import math
num = 1
while 1:
    diameter, rpm, sec = map(float, input().split())

    if rpm == 0:
        break

    dist = diameter * math.pi * rpm / 63360
    avg = dist / sec * 3600
    print(f"Trip #{num}: {round(dist, 2):.2f} {round(avg, 2):.2f}")
    num += 1
