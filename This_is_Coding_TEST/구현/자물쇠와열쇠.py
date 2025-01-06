# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
  n = len(a) # 행 길이
  m = len(a[0]) # 열 길이
  result = [[0] * n for _ in range(m)] # 결과 리스트
  for i in range(n):
    for j in range(m):
      result[j][n - i - 1] = a[i][j]
  return result

# 자물쇠의 중간 부분이 1인지 확인
def check(new_lock):
  lock_length = len(new_lock) // 3
  for i in range(lock_length, lock_length * 2):
    for j in range(lock_length, lock_length * 2):
      if new_lock[i][j] != 1:
        return False
  return True

def solution(key, lock):
  n = len(lock)
  m = len(key)
  # 3배로 자물쇠 크기 키우기
  new_lock = [[0] * (n * 3) for _ in range(n * 3)]
  # 새 자물쇠 중앙 부에 기존 자물쇠 넣기
  for i in range(n):
    for j in range(j):
      new_lock[i + n][j + n] = lock[i][j]

  # 4가지 방향 체크
  for rotation in range(4):
    key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
    for x in range(n * 2):
      for y in range(n * 2):
        # 자물쇠에 열쇠 끼어넣기
        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + j] += key[i][j]
        # 새로운 자물쇠에 열쇠가 정확히 맞는지 검사
        if check(new_lock) == True:
          return True
        # 자물쇠에서 열쇠를 다시 빼기
        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + j] -= key[i][j]
  return False
