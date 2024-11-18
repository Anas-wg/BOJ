import sys
import heapq

N = int(sys.stdin.readline())
pq = []
for _ in range(N):
  x = int(sys.stdin.readline().rstrip())
  if x:
    heapq.heappush(pq, (abs(x), x))
  else:
    if pq: 
      print(heapq.heappop(pq)[1])
    else:
      print(0)