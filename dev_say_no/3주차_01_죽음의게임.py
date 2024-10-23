import sys
N , K = map(int, sys.stdin.readline().split(" "))


sooljari = []

for i in range(N):
  start = i
  next = int(sys.stdin.readline().rstrip())
  sooljari.append([i , next])

print(sooljari)



