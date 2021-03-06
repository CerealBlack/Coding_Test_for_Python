# 떡의 개수와 요청한 떡의 길이 입력 
n, m = list(map(int, input().split())) 
# 각 떡의 개별 높이 입력 
array = list(map(int, input().split())) 

# 이진 탐색을 위한 시작점과 끝점 설정 
start = 0 
end = max(array) 

# 이진 탐색 수행(반복적) 
result = 0 
while start <= end: 
    total = 0 
    # mid가 원하는 m에 맞추어 자를 수 있는 최대 높이 값 
    mid = (start + end) // 2 
    for x in array: 
        # 잘랐을 때의 떡의 양 계산 
        if x > mid: 
            total += x - mid 
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색) 
    if total < m: 
        end = mid - 1 
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색) 
    else: 
        # 적어도 m만큼은 떡을 얻어야 해서 else일때 절단기 길이를 저장, 그 후 반복으로 최적값 찾음 
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록 
        start = mid + 1 
print(result) 
