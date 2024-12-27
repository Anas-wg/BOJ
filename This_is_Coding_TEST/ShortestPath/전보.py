import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

N ,M ,C = map(int, input().split())

# 연결정보 담길 그래프
graph = [[]for i in range(N + 1)]
# 무한으로 거리 초기화
distance = [INF] * (N + 1)

# 그래프 만들기
for i in range(M):
  X, Y, Z = map(int, input().split())
  graph[X].append((Y, Z))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(C)
ans = 0
result = []

for i in range(1 ,N + 1):
  if distance[i] != INF and distance[i] != 0:
    ans +=1
    result.append(distance[i])

print(graph)
print(distance)
print(ans, end=' ')
print(max(result))
