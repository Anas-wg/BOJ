import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())  
adj_list = [[] for _ in range(N+1)]  
visited = [False for _ in range(N+1)]  

# 간선 정보 입력 받기
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

# dfs 탐색
def dfs(graph, v, visited):
    visited[v] = True
    for next_v in adj_list[v]:
    	if not visited[next_v]:
        	dfs(adj_list, next_v, visited)


# 결과  출력

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(adj_list, i, visited)
        count += 1
print(count)