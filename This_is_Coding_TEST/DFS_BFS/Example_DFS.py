
def depth_first_search(graph, v, visited):
  # 현재 노드 방문처리
  visited[v] = True
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  # (2차원 리스트 형태기 때문에 for 문으로 순회하여 방문)
  for i in graph[v]:
    if not visited[i]:
      depth_first_search(graph, i, visited)

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

depth_first_search(graph, 1, visited)