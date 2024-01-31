import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
ch = [[0] * M for _ in range(N)]

campus = []
Queue = deque()

for i in range(N):
  campus.append(list(map(str, sys.stdin.readline().strip())))
  for j in range(len(campus[i])):
    if campus[i][j] == 'I':
      Queue.append([i,j])
      ch[i][j] = 1

answer = 0

# BFS -> 
while Queue:
  for _ in range(len(Queue)):
    x, y = Queue.popleft()
    for i in range(4):
      nx,ny = x + dx[i], y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < M and ch[nx][ny] == 0 and campus[nx][ny] != 'X':
        if campus[nx][ny] == 'P':
          answer += 1
        ch[nx][ny] = 1
        Queue.append([nx, ny])

if answer:
  print(answer)

else:
  print('TT')