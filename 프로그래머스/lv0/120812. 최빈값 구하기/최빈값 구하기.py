def solution(array):
    count = [0,0]
    array = sorted(array, key=lambda x : array.count(x), reverse=True)
    for i in array:
        if count[0]!=i and array.count(i) == count[1]:
            return -1
        elif array.count(i) > count[1]:
            count = [i, array.count(i)]
    return count[0]