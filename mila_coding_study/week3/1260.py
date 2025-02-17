import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 정점 번호가 작은 것부터 방문해야 하므로 정렬
for i in range(1, N + 1):
    graph[i].sort()

def dfs(v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

def bfs(v, visited):
    queue = deque([v])
    visited[v] = True  # 방문 체크를 큐에 넣을 때 수행
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True  # 방문 체크를 큐에 추가할 때 수행

# 방문 배열 초기화
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

dfs(V, visited_dfs)
print()  # 줄바꿈
bfs(V, visited_bfs)
print()
