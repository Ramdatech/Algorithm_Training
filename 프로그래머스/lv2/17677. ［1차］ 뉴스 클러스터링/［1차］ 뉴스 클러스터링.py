def solution(str1, str2):
    answer = [0, 0]
    ls_1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    ls_2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    for i in list(set(ls_1) | set(ls_2)):
        answer[0] += min(ls_1.count(i), ls_2.count(i))
        answer[1] += max(ls_1.count(i), ls_2.count(i))
    return 65536 if answer[1] == 0 else (answer[0]/answer[1]*65536)//1