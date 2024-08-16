H, W, N, M = map(int, input().split())
r = (H + N) // (N + 1)
c = (W + M) // (M + 1)
print(r*c)