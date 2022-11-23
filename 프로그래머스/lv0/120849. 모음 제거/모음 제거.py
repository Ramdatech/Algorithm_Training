def solution(my_string):
    answer = [x for x in my_string if x not in ['a','e','i','o','u']]
    return "".join(answer)