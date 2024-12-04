import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
count = 0
# 그래프 생성
for i in range(M):
  u, v = map(int, sys.stdin.readline().rstrip().split())
  graph[u].append(v)
  graph[v].append(u)

# 그래프 탐색

def dfs(node):
    visited[node] = True
    for next_node in graph[node]:
       if not visited[next_node]:
          dfs(next_node)

for i in range(1, N+1):
   if not visited[i]:
      dfs(i)
      count += 1

print(count)
    