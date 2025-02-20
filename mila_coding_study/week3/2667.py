import sys
input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = []
answer = []
for _ in range(N):
  line = list(map(int, input().rstrip()))
  graph.append(line)

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  graph[x][y] = 0  # 방문 처리
  count = 1  # 단지 크기 카운트

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
        graph[nx][ny] = 0  # 방문 처리
        queue.append((nx, ny))
        count += 1  # 단지 크기 증가

  return count  # 단지 크기 반환

for x in range(N):
  for y in range(N):
    if graph[x][y] == 1:
      answer.append(bfs(x, y))  # 각 단지 크기를 리스트에 추가

# 오름차순 정렬 후 출력
answer.sort()

print(len(answer))  # 총 단지 수 출력
for size in answer:
  print(size)  # 각 단지 크기 출력
