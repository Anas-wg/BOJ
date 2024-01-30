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
# while Queue: