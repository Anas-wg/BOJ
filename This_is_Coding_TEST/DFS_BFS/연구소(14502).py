N, M = map(int, input().split())

data =[] # 초기 맵 리스트
temp = [[0] * M for _ in range(N)] # 벽 설치한 후 맵 리스트

# 그래프 입력받기
for _ in range(N):
  data.append(list(map(int, input().split())))

# dx, dy -> 4가지 이동방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS 를 이용하여 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
  for i in range(4):
    nx = x + dy[i]
    ny = y + dy[i]
    # 상, 하, 좌, 우 중 바이러스가 퍼질 수 있는 경우
    if nx >= 0 and nx < N and ny >= 0 and ny < N:
      if temp[nx][ny] == 0: # 빈칸이라면
        temp[nx][ny] = 2 # 바이러스 배치
        virus(ny, nx) # 다시 확산 진행

def get_safe():
  score = 0
  for i in range(N):
    for j in range(M):
      if temp[i][j] == 0:
        score += 1

# 깊이 우선 탐색을 통해서 울타리 설치 & 매번 안전영역의 크기 계산
def dfs(count):
  global result
  # 울타리가 3개 설치된 경우
  if count == 3:
    for i in range(N):
      for j in range(M):
        temp[i][j] = data[i][j]
    for i in range(N):
      for j in range(M):
        if temp[i][j] == 2: # 바이러스 위치에서 확산
          virus(i ,j)
    result = max(result, get_safe())
    return
  # 빈 공간에 울타리 설치
  for i in range(N):
    for j in range(M):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        data[i][j] = 0
        count += 1

dfs(0)
print(result)