import sys

N = int(sys.stdin.readline().rstrip())
data = []
for i in range(N):
  x,y = map(int, sys.stdin.readline().rstrip().split(' '))
  data.append([x,y])

for elem in data:
  place = 1
  for comp in data:
    if elem[0] < comp[0] and elem[1] < comp[1]:
      place += 1
  print(place, end=' ')