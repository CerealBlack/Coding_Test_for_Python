def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for number in range(1, N + 1): # 가장 작은 수가 1이어서 1부터 시작 
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(number)
        
        # 실패율 계산
        if length == 0: # N = 1, stages가 None인 경우를 위해서 
            fail = 0
        else:
            fail = count / length # 정수 나누기 연산으로 하면 모두 0이 나오기 때문에
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((number, fail)) 
        length -= count 
    
    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer.sort(key = lambda x : -x[1]) 
    
    answer = [ number[0] for number in answer ]
    return answer

stages = [2, 1, 2, 6, 2, 4, 3, 3]
# stages = [] 
print(solution(5, stages))  
# print(solution(0, stages ))