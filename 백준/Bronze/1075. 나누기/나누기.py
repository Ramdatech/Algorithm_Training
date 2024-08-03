n, d = int(input())//100*100, int(input())
print("00" if n%d == 0 else str(d-n%d).zfill(2))