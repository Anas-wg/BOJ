# 순차 탐색
def sequential_search(n, target, array):
  # 각 원소 하나씩 확인
  for i in range(n):
    if array[i] == target: # 현재 원소가 타겟과 동일하다면
      return i + 1 # 현재 인덱스를 반환
    
# 이진 탐색(재귀 활용)
def binary_recursion(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  # 찾은 경우 중간점 인덱스를 반환
  if array[mid] == target:
    return mid
  # 중간점 보다 찾으려는 값이 작은 경우 왼쪽만 확인
  elif array[mid] > target:
    return binary_recursion(array, target, start, mid - 1)
  # 중간점보다 찾으려는 값이 큰 경우 오른쪽만 확인
  else:
    return binary_recursion(array, target, mid + 1, end)
  
# 이진 탐색(단순 반복문)
def binary_iteration(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid # 찾은 경우
    elif array[mid] > target:
      end = mid - 1 # 중간점보다 찾으려는 값이 작은 경우
    else:
      start = mid + 1 # 중간점보다 찾으려는 값이 큰 경우
  return None



    