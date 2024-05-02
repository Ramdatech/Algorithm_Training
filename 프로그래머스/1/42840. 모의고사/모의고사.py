def solution(answers):
#     answer = [0, 0, 0]
#     testers = ["1 2 3 4 5".split(), '2 1 2 3 2 4 2 5'.split(), '3 3 1 1 2 2 4 4 5 5'.split()]
#     for m, tester in enumerate(testers) :
#         for idx,ans in enumerate(answers):
#             if tester[idx%len(tester)] == str(ans) :
#                 answer[m] += 1
    
#     result = []
#     for idx, i in enumerate(answer):
#         if i == max(answer) :
#             result.append(idx+1)
            
#     return result
		# 각 수험생 1,2,3의 스코어보드, 빈 딕셔너리 선언
    result = {1:0, 2:0, 3:0}
    # 각 수험생이 찍는 답 선언
    test_ans = ["1 2 3 4 5".split(), '2 1 2 3 2 4 2 5'.split(), '3 3 1 1 2 2 4 4 5 5'.split()]
    # 각 리스트 요소를 숫자로 변경
    test_ans = [list(map(int, x)) for x in test_ans]
    
    # 반복문 돌입 (답 기준)
    for idx, t_ans in enumerate(test_ans) : 
        total = t_ans * (len(answers)//len(t_ans)+1) # 전체 시험문제 길이와 수험생 답 길이 일치
        for a1,a2 in zip(total, answers) : 
            if a1 == a2 :
                result[idx+1] += 1		# 답이 맞을 때마다 수험생 점수 +1
    
    # 수험생의 최대 점수 반환
    mx = max(result.values())
    # 최대 점수를 가진 수험생 리스트로 반환
    return [x for x in result if result[x] == mx]