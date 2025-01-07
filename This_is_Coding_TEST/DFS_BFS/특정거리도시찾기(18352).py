from collections import deque

n, m, k, x = map(int,input().split())
graph = [[] for _ in range(n + 1)]

# 그래프 입력
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (n - 1)
distance[x] = 0 # 출발 도시까지 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x]) # x를 시작점으로,
while q:
  now = q.popleft() 
  # 현재 도시에서 이동 가능한 모든 도시 확인
  for next_node in graph[now]:
    # 아직 미방문 도시라면
    if distance[next_node] == -1:
      # 최단 거리 갱신
      distance[next_node] = distance[now] + 1
      q.append(next_node)

# 최단 거리가 K인 도시의 번호를 오름 차순 출력
check = False
for i in range(1, n + 1):
  if distance[i] == k:
    print(i)
    check = True
  if check == False:
    print(-1)
