from collections import deque

adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1


def dfs(now):
  for nxt in range(13):
    if adj[now][nxt]:
      dfs(nxt)
  

dfs(0)

def bfs():
  dq = deque()
  dq.append(0)
  while dq:
    # 현재 노드 pop
    now = dq.popleft()
    for nxt in range(13):
    # 현재 노드와 연결된 다음 노드를 큐에 삽입
      if adj[now][nxt]:
        dq.append(nxt)

bfs()


dx ,dy = (0,1,0,-1),(1,0,-1,0)
chk = [[False] * 100 for _ in range(100)]
N = int(input)


def is_valid_coord(x, y):
  return 0 <= y < N and 0 <= x < N

def bfs (start_y, start_x):
  q = deque()
  q.append((start_y, start_x))
  while len(q) > 0:
    y, x = q.popleft()
    chk[y][x] = True
    # 4방향 간선
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      # 벽이 아닌지, 방문 여부 확인
      if is_valid_coord(ny,nx) and not chk[ny][nx]:
        q.append((ny,nx))