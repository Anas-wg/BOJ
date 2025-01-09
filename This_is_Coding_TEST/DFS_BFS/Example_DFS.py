# DFS 메서드 정의
def dfs(graph, v, visted):
  # 현재 노드 방문 처리
  visted[v] = True
  # 방문 시 출력
  print(v, end= ' ')
  # 현재 노드와 연결된 다른 노드 재귀적으로 방문
  for i in graph[v]:
    # 방문하지 않았다면
    if not visted[i]:
      # DFS 재귀적 수행
      dfs(graph,i,visted)

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
dfs(graph, 1, visited) # 1 2 3 4 5 순