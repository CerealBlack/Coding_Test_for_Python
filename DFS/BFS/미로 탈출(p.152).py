from collections import deque

n, m = map(int, input().split())
wall = [ [0] * m for _ in range(n) ]

for i in range(n):
    wall[i] = list(map(int, input()))

dx = [ -1, 1, 0, 0 ]
dy = [ 0, 0, -1, 1 ]

def bfs(x, y):
    # 큐(queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if wall[nx][ny] == 0:
                continue
            if wall[nx][ny] == 1:
                wall[nx][ny] = wall[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return wall[n-1][m-1]
print(bfs(0, 0)) 