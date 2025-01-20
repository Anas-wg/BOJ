INF = int(1e9)

N = int(input())
M = int(input())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
  for b in range(1, N + 1):
    if a == b :
      graph[a][b] = 0

for _ in range(M):
  a, b, c = map(int, input().split())
  if graph[a][b] != INF and graph[a][b] != 0:
    graph[a][b] = min(c, graph[a][b])
  else:
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
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()