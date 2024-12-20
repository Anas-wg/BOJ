from collections import deque

def dfs(graph, v ,visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

visited = [False] * 9

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue :
    v = queue.popleft()
    print(v, end= ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True


