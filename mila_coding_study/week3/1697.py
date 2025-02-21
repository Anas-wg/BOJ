from collections import deque

def bfs(n, k):
    if n >= k:
        return n - k  # 뒤로 가는 경우는 -1씩 하면 되므로
    
    max_size = 100001  # 문제에서 주어진 범위
    visited = [-1] * max_size
    queue = deque([n])
    visited[n] = 0  # 시작 위치 방문
    
    while queue:
        x = queue.popleft()
        
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx < max_size and visited[nx] == -1:  # 방문하지 않았다면
                visited[nx] = visited[x] + 1
                queue.append(nx)
                
                if nx == k:
                    return visited[nx]

n, k = map(int, input().split())
print(bfs(n, k))
