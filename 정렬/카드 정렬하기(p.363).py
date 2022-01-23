import heapq

n = int(input()) 

# 힙(heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n): 
    data = int(input())
    heapq.heappush(heap, data) 

result = 0

# 힙(heap)에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap) 
    two = heapq.heappop(heap) 
    # 카드 묶음을 합쳐서 다시 삽입
    sum = one + two
    result += sum
    heapq.heappush(heap, sum) 

print(result) 