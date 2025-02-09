# N * M 크기 얼음틀
# 서로 연결된 0의 개수 구하기

# 1. 입력받기(N ,M, graph)
N, M = map(int, input().split())

graph = []

for i in range(N):
  line = list(map(int,input()))
  graph.append(line)
# 2. 아이스크림 개수 찾기 -> 0 이 서로 연결된 경우
# DFS 활용 => 칸이 0일 경우, 1일 경우 
# DFS 설계
# 1. 0인 칸을 찾는 과정

def dfs(x, y):
  # 주어진 범위 벗어나는 경우 즉시 종료
  if x <= -1 or x >= N or y <= -1 or y >= N:
    return False
  # 현재 노드 미방문시
  if graph[x][y] == 0:
    # 방문처리
    graph[x][y] == 1
    # 상, 하, 좌, 우 dfs
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

result = 0
for i in range(N):
  for j in range(M):
    if dfs(i, j) == True:
      result += 1

print (result)


  