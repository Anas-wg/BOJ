n = int(input())
k = int(input())

data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

for _ in range(k):
  a, b = map(int, input().split())
  data[a][b] = 1 # 사과 위치시 1로 표시

l = int(input())
for _ in range(l):
  # c는 문자열이니까...
  x, c = input().split()
  info.append((int(x), c))

# 오른쪽 바라봄 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0,-1, 0]

def turn (direction, c):
  if c == "L":
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
  return direction

def simulate():
  x, y = 1, 1 # 뱀의 머리 위치
  data[x][y] = 2 # 뱀이 위치하면 2로 표시
  direction = 0 # 처음엔 동쪽 (x, y + 1)
  time = 0 # 초 시간
  index = 0 # 다음 회전할 정보
  q = [(x, y)] # 뱀이 차지하고 있는 위치
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 맵 안에 있고, 뱀의 몸통이 없다면
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
      if data[nx][ny] == 0:
        data[nx][ny] = 2
        q.append((nx, ny)) # 꼬리가 앞쪽에 오게끔?
        # 지나간 자리는 다시 원상 복구
        px, py = q.pop(0)
        data[px][py] = 0 

      # 만약 사과가 있는 경우 머리만 이동, 꼬리는 그대로
      if data[nx][ny] == 1:
        data[nx][ny] = 2
        q.append((nx,ny))

      else:
        # 벽이나 몸통과 부딪힌 경우
        time += 1
        break
    x, y = nx, ny #다음 위치로 머리 이동
    time += 1
    if index < 1 and time == info[index][0]:
      # 회전할 시간일 경우 회전
      direction = turn(direction, info[index][1])
      index += 1
  return time

print(simulate())

