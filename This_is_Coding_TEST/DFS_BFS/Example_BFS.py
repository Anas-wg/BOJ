from collections import deque

def Breadth_First_Search(graph, start, visited):
  # deque 라이브러리 활용하여 큐 구현
  q = deque([start])
  # 시작 노드 방문처리
  visited[start] = True
  while q:
    # 노드 하나 꺼내기
    v = q.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
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

Breadth_First_Search(graph, 1, visited)