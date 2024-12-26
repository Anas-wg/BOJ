INF = int(1e9)

# 노드 개수 및 간선 개수 입력받기
N = int(input())
M = int(input())

# 2차원 리스트(그래프)를 만들고 모든 값 무한으로 초기화
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기자신 -> 자기자신 비용은 0으로 초기화
for a in range(1, N + 1):
  for b in range(1, N + 1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받고 그 값으로 초기화
for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, N + 1):
  for a in range(1, N + 1):
    for b in range(1, N + 1):
      # 점화식 적용
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, N + 1):
  for b in range(1, N + 1):
    if graph[a][b] == INF:
      print("INF", end=" ")
    else:
      print(graph[a][b], end =" ")
  print()