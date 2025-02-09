from collections import deque

def breadth_first_search(graph, start, visited):
  # 큐 생성(deque 자료형 활용) 및 시작노드 삽입
  queue = deque([start])
  # 큐가 빌때 까지
  while queue:
    # 노드 꺼내기
    v = queue.popleft()
    print(v, end= ' ')
    visited[start] = True
    # 꺼낸 노드의 인접노드 중
    for i in graph[v]:
      # 미방문 노드를 큐에 삽입
      if not visited[i]:
        queue.append(i)
        # 방문 처리
        visited[i] = True


graph = [
  [], # 0번 노드는 없으니까
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1 , 7]
]

visited = [False] * 9

breadth_first_search(graph, 1, visited)