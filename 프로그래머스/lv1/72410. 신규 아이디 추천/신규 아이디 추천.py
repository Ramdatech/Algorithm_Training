import re

def solution(new_id):
    new_id = new_id.lower()
    answer = ''.join([x for x in new_id if x.isdecimal() or x.isalpha() or x in '- _ .'.split()])
    print(answer)
    answer = re.sub('[.]+', ".", answer)
    answer = ''.join(["" if x=='.' and (idx==0 or idx==len(answer)-1) else x for idx, x in enumerate(answer)])
    if answer == '' : answer += 'a'
    if len(answer) >= 16 : answer = answer[:15]
    answer = ''.join(["" if x=='.' and (idx==0 or idx==len(answer)-1) else x for idx, x in enumerate(answer)])
    if len(answer) <= 2 : answer += answer[-1] * (3-len(answer))
    
    return answer