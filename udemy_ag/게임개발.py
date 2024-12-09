# 입력받기
N , M  = map(int, input().split())
x, y ,d = map(int, input().split())

arr = []
for i in range(M):
  line = list(map(int, input().split()))
  arr.append(line)

visited = [[False] * M for _ in range(N)]

# dx, dy
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0] 

