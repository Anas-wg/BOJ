M = int(input())

cur_location = 1

for _ in range(M):
  X, Y = map(int, input().split())
  if cur_location == X:
    cur_location = Y
  elif cur_location == Y: 
    cur_location = X

  
if cur_location:
  print(cur_location)
else:
  print(-1)