def solution(s, n):
    answer = ''
    for i in s :
        if i.islower(): answer += chr(97+(ord(i)+n-97)%26)
        elif i.isupper(): answer += chr(65+(ord(i)+n-65)%26)
        else : answer += i
    return answer