# 입력받기
N, M = map(int, input().split())

# 2차원 리스트 맵정보 입력받기
graph = []
for i in range(N):
  graph.append(list(map(int, input())))

# DFS를 활용하여 특정 노드 방문 후 연결된 모든 노드 방문
def dfs(x, y):
  # 범위 이탈시 종료
  if x <= -1 or x >= N or y <= -1 or y >= M:
    return False
  # 현재 노드가 방문X , 1이라면 탐색 X
  if graph[x][y] == 0:
    # 1로 바꾸어 방문처리
    graph[x][y] = 1
    # 상, 하 ,좌, 우 위치 모두 재귀 호출
    dfs(x - 1, y)
    dfs(x, y- 1)
    dfs(x + 1, y)
    dfs(x, y+ 1)
    return True
  return False

result = 0
for i in range(N):
  for j in range(M):
    if dfs(i, j) == True:
      result += 1

print(result)
