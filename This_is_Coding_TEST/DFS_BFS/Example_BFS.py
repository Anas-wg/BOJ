from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
  # Queue 구현을 위해 deque 라이브러리 활용
  # 시작 노드 삽입
  queue = deque([start])
  # 시작 노드 방문처리
  visited[start] = True
  # 큐 빌때 까지 반복
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    # 인접한 노드 순회
    for i in graph[v]:
      # 미방문 노드라면
      if not visited[i]:
        # 큐에 삽입
        queue.append(i)
        # 방문처리
        visited[i] = True


# 2차원 리스트로 graph 표현 (인덱스 맞추기 위해 0 비움)
graph = [
  [],
  [2,3],
  [1],
  [1,4,5],
  [3,5],
  [3,4]
]

# 방문 정보 기록 리스트
visited = [False] *  6

# 1부터 DFS 탐색 시작
bfs(graph, 1, visited) # 1 2 3 4 5 순