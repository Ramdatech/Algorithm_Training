def solution(polynomial):
    array = polynomial.split(" + ")
    answer = [x if "x" not in x else '10000' if len(x)==1 else x.replace("x", "*10000") for x in array]
    answer = eval('+'.join(answer))
    a, b = answer//10000 if answer//10000!=1 else "", answer%10000
    return f"{a}x + {b}" if a!=0 and b!=0 else f"{a}x" if a!=0 and b==0 else  f"{b}"