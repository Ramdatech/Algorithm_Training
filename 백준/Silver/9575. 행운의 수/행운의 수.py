def func(test_cases):
    res = []
    for case in test_cases:
        A, B, C = case
        ret = set()

        for a in A:
            for b in B:
                for c in C:
                    total = a + b + c
                    if all(c in '58' for c in str(total)) :
                        ret.add(total)

        res.append(len(ret))
    return res



n = int(input().strip())
nums = []
for _ in range(n):
    res = []
    for _ in range(3):
        tmp = int(input().strip())
        res.append(list(map(int, input().strip().split())))

    nums.append(res)

res = func(nums)
print(*res, sep='\n')