INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력 받기
N , M = map(int, input().split())
# 2차원 리스트 만들고 모든 값을 무한으로 초기화
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기자신 -> 자기자신은 0
for a in range(1, N + 1):
  for b in range(1, N + 1):
    if a == b:
      graph[a][b] = 0

for _ in range(M):
  # A,B가 서로에게 가는 비용 1이라 설정
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

X, K = map(int, input().split())

# 점화식에 따른 플로이드 알고리즘 수행
for K in range(1, N + 1):
  for a in range(1, N + 1):
    for b in range(1, N + 1):
      graph[a][b] = min(graph[a][b],graph[a][K]+graph[K][b])

distance = graph[1][K] + graph[K][X]

if distance >= INF:
  print(-1)
else: 
  print(distance)
