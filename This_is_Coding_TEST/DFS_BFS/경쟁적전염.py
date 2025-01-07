from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보
data = [] # 바이러스 대한 정보

for i in range(n):
  # 보드 정보 한줄로 입력
  graph.append(list(map(int, input().split())))
  for j in range(n):
    # 해당 위치에 바이러스 존재하는 경우
    if graph[i][j] != 0:
      data.append((graph[i][j], 0, i , j))

# 정렬 이후 큐로 옮기기(낮은 번호의 바이러스가 먼저 종식)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 진행 => Queue 에서 바이러스를 하나씩 꺼내면서 실행
while q: 
  virus, s, x, y = q.popleft()
  # 정확히 S초 지나거나 큐가 빌때까지 반복
  if s == target_s:
    break
  # 현재 위치에서 주변 4가지 위치를 확인
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 해당 위치로 이동할 수 있는 경우
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      # 아직 방문안했다면 그 위치에 바이러스 넣기
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])