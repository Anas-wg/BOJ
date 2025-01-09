from itertools import combinations

n = int(input())
board = [] # 복도 정보
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
  board.append(list(input().split()))
  for j in range(n):
    # 선생님 위치 저장
    if board[i][j] == 'T':
      teachers.append((i, j))
    # 장애물 설치 가능한 위치 저장
    if board[i][j] == 'X':
      spaces.append((i, j))

# 특정 방향을 감시 진행(학생 발견시 True) 
def watch(x, y, direction):
  # 왼쪽 방향
  if direction == 0:
    while y >= 0:
      if board[x][y] == 'S': # 학생 있는 경우
        return True
      if board[x][y] == 'O': # 장애물 있는 경우
        return False
      y -= 1
    # 오른쪽 방향
    if direction == 1:
      while y < n:
        if board[x][y] == 'S': # 학생 있는 경우
          return True
        if board[x][y] == 'O': # 장애물 있는 경우
          return False
        y += 1
    # 위쪽 방향 감시
    if direction == 2:
      while x >= 0:
        if board[x][y] == 'S':
          return True
        if board[x][y] == 'O':
          return False
        x -= 1
    # 아래쪽 방향
    if direction == 3:
      while x < n :
        if board[x][y] == 'S':
          return True
        if board[x][y] == 'O':
          return False
        x += 1
  return False

# 장애물 설치 이후, 한명이라도 학생 감지되는지 확인
def process():
  # 모든 선생님의 위치 하나씩 체크
  for  x, y in teachers:
    # 4가지 방향으로 학생 감지 가능한지 확인
    for i in range(4):
      if watch(x, y, i):
        return True
  return False

find = False # 학생이 한명도 감지되지 않도록 설치할 수 있는지 여부

# 빈 공간서 3개를 뽑는 모든 조합 확인
for data in combinations(spaces, 3):
  # 장애물 설치해보기
  for x, y in data:
    board[x][y] = 'O'
  # 학생이 한 명도 감지 X
  if not process():
    find = True
    break
  # 설치된 장애물 다시 없애기
  for x, y in data:
    board[x][y] == 'X'

if find:
  print('YES')
else:
  print('NO')  
    
      