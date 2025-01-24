import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한

# 입력받기
N, M = map(int, input().split())
start = int(input()) # 시작노드 입력
# 각 노드별로 연결된 노드 정보 담길 그래프
graph = [[]for i in range(N + 1)]
# 무한으로 거리 초기화
distance = [INF] * (N + 1)

# 모든 간선 정보 입력
for i in range(M):
  a, b, c = map(int, input().split()) # 1 2 2 
  # (다음 거리, 노드)
  graph[a].append((b, c)) # [[2, 2]] 입력


# 다익스트라
def dijkstra(start):
  q = [] # Proirity Queue
  # q리스트에 (거리, 노드) 형식으로 저장
  heapq.heappush(q, (0, start))
  # 출발노드는 0
  distance[start] = 0
  # 우선순위 큐가 빌때까지
  while q:
    # 가장 짧은 경로 가진 원소 꺼내기
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리되었다면 무시
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접 노드들 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은경우 -> 갱신
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, N + 1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])
    
