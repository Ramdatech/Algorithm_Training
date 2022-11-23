temp = input().split()
ans = [1, 1, 2, 2, 2, 8]
res = [str(ans[idx]-int(x)) for idx, x in enumerate(temp)]
print(" ".join(res))