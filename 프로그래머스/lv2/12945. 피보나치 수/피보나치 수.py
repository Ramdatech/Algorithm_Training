# fb = {0 : 0,
#       1 : 1,
#       2 : 1,}
# def fb_number(n):
#     if n in fb.keys():
#         return fb[n]%1234567
#     else :
#         fb[n] = fb_number(n-1) + fb_number(n-2)
#         return fb[n]%1234567

fb = [0, 1, 1]
def fb_number(n):
    if n <= 2 :
        return fb[n]
    while len(fb) <= n :
        var = fb[-1] + fb[-2]
        fb.append(var%1234567)
    return fb[-1]
    
def solution(n):
    answer = fb_number(n)
    
    return answer