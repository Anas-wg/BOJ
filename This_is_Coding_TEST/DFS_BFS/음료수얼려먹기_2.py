N, M = map(int, input().split())

graph = []

for i in range(N):
  line = list(map(int, input())) # 2차원 리스트 만들기
  graph.append(line)

# 좌표개념으로 생각
def dfs(x, y):
  # 범위를 벗어난 경우
  if x <= -1 or x >= N or y <= -1 or y >= N:
    return False
  # 아직 미방문 시
  if graph[x][y] == 0:
      # 1로 바꾸어 방문처리
      graph[x][y] = 1
      # 상, 하, 좌, 우 dfs 수행
      dfs(x - 1, y) # left
      dfs(x + 1, y) # right
      dfs(x, y + 1) # up
      dfs(x, y = 1) # down
      return True
  return False

result = 0
for i in range(N):
   for j in range(M):
      # 0,0 부터 N,M 까지 모든 지점 서 수행
      if dfs(i, j) == True:
         result += 1

print(result)