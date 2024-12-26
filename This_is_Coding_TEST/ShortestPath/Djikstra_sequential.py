# 순차탐색을 통해 미방문 노드 중 최단 거리가 가장 짧은 노드 선택
# Time Complextity : O(V^2)

import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 ,간선의 개수 입력 받기
N , M = map(int, input().split())
# 시작노드 번호 입력
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트(최단거리 Table)
graph = [[] for i in range(N + 1)]
# 방문한 적 있는지 체크하는 리스트
visited = [False] * (N + 1)
# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (N + 1)

# 모든 간선 정보 입력받기
for _ in range(M):
  # a -- c ---> b , a에서 b로 가는 비용이 c
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

# 방문하지 않은 노드 중 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, N +1):
    # 리스트 내 각 노드를 하나씩 돌면서 기존의 최단 거리보다 짧다면(작다면) min_val 교체
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

# 다익스트라 
def dijkstra(start):
    distance[start] = 0  # 시작 노드의 거리는 0
    visited[start] = True  # 시작 노드는 방문 처리
    for j in graph[start]:
        distance[j[0]] = j[1]  # 시작 노드와 직접 연결된 노드들의 거리 갱신

    for _ in range(N - 1):  # 모든 노드에 대해 반복
        now = get_smallest_node()  # 방문하지 않은 노드 중 최단 거리 노드 선택
        visited[now] = True  # 선택된 노드 방문 처리
        for j in graph[now]:  # 현재 노드와 연결된 노드들 확인
            cost = distance[now] + j[1]  # 현재 노드를 거쳐 가는 거리 계산
            if cost < distance[j[0]]:  # 더 짧은 거리가 발견되면 갱신
                distance[j[0]] = cost

# 다익스트라 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, N + 1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    # 도달할 수 있는 경우
    print(distance[i])