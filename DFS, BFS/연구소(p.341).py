n, m = map(int, input().split())
# 초기 맵 리스트
graph = [ [] * m for _ in range(n) ]
# 벽을 설치한 뒤의 맵 리스트
temp = [ [0] *m for _ in range(n) ] # 0안 넣어주면 인덱스 에러 발생.

for i in range(n):
    graph[i] = list(map(int, input().split()))

# 북, 동, 남, 서
dx = [ -1, 0, 1, 0 ]
dy = [ 0, 1, 0, -1 ]

result = 0
# dfs를 이용한 바이러스 전파시키는 메서드 
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기를 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score 

# dfs를 이용해 울타리를 설치하면서 안전영역의 크기 계산
def dfs(count): # count = 0 이때 선언
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        # 각 바이러스의 위치에서 전파 진행  
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1
# dfs는 스택의 개념을 이용 (완전탐색)
dfs(0)
print(result) 
