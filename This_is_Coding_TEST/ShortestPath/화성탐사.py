import heapq
import sys
input = sys.stdin.readline
INF = int(129) # 거리값 초기화 위한 무한대 값 할당

# 상, 하, 좌, 우기 때문에 dx, dy 활용
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, 1]

# Testcase 입력받기
T = int(input())

for tc in range(T):
  # 노드 개수 입력
  N = int(input())
  # 전체 맵 정보 입력받기
  graph = []
  for i in graph(N):
    graph.append(list(int, input().split()))

  # 최단 거리 저장 테이블 무한으로 초기화
  distance = [[INF] * N for _ in range(N)]

  # 시작 위치는 (0, 0)
  x, y = 0, 0
  # 시작 노드로 가기 위한 비용(0, 0) 위치 값으로 설정, 큐 삽입
  q = [(graph[x][y], x, y)] # 우선순위 큐니까 노드의 비용 적은 거 부터 진행
  distance[x][y] = graph[x][y]

  # 다익스트라 알고리즘 수행
  while q:
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, x, y = heapq.heappop(q)
    if distance[x][y] < dist:
      continue
    # 현재 노드가 이미 처리되었다면 무시
    if distance[x][y] < dist:
      continue
    # 현재 노드가 인접한 다른 노드 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 맵의 범위 벗어나는 경우 무시
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
      cost = dist + graph[x][y]
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 경우가 더 짧을 때
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost
        heapq.heappush(q, (cost, nx, ny))

print(distance[N -1][N - 1])

