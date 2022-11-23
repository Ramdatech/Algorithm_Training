def solution(cipher, code):
    answer = [cipher[x] for x in range(len(cipher)) if (x+1)%code == 0]
    return ''.join(answer)