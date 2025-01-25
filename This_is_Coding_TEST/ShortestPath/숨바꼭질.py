import heapq
import sys
input = sys.stdin.readline

N , M = map(int, input().split())
INF = int(1e9)

distance = [INF] * (N + 1) # 거리 테이블 초기화
graph = [[] for _ in range(N + 1)] # 노드에 대한 정보 담는 리스트

for _ in range(M):
  a, b = map(int, input().split())
  # 양방향 이니까
  graph[a].append((b, 1))
  graph[b].append((a, 1))

def dijiksta(start):
  q = []
  heapq.heappush(q,(0, start))
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

# 다익스트라 알고리즘 수행
dijiksta(1)

max_node = 0 # 동빈이가 숨을 노드 번호
max_distance = 0  # 가장 먼 노드와의 거리
result = []

for i in range(1, N + 1):
  if max_distance < distance[i]:
      max_node = i
      max_distance = distance[i]
      result = [max_node]
  elif max_distance == distance[i]:
     result.append(i)
  
print(max_node, max_distance,len(result))
     

                    

