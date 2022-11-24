def binize(x,n) :
    return str(bin(x)[2:]).zfill(n)

def solution(n, arr1, arr2):
    answer = [''.join(["#" if int(x)|int(y) == 1 else " " for x, y in zip(binize(x,n),binize(y,n))]) for x,y in zip(arr1,arr2)]
    return answer