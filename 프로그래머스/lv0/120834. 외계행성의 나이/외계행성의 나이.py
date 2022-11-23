def solution(age):
    return''.join([chr(int(x)+ord('a')) for x in list(str(age))])