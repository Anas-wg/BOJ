# 정렬된 수열에서 값이 x 인 원소의 개수를 세는 메서드
def count_by_value(array, x):
  # 데이터의 개수
  n = len(array)
  
  # x가 처음 등장한 인덱스를 계산
  a = first(array ,x, 0, n - 1)

  # 수열에 x 없는 경우
  if a == None:
    return 0 # 값이 x인 원소자체가 없으니 a만 보면 됨

  # x가 마지막으로 등장한 인덱스 계산
  b = last(array, x, 0, n - 1)

  # 개수를 반환
  return b - a + 1

# 처음 x의 인덱스 찾는 메서드
def first(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  # x 중 가장 왼쪽에 있는 경우만 인덱스 반환
  if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
    return mid
  # 중간보다 찾고자 하는 값이 적거나 같은 경우 왼쪽으로
  elif array[mid] >= target:
    return first(array, target, start, mid - 1)
  else: 
    return first(array, target, mid + 1, end)
      
# 마지막 위치 찾는 이진 탐색 메서드

def last(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  # x 중 가장 우측에 있는 경우만 인덱스 반환
  if (mid == n - 1 or target < array[mid + 1]) and array[mid]== target:
    return mid
  # 중간보다 찾고자 하는 값이 적거나 같은 경우 왼쪽으로
  elif array[mid] > target:
    return last(array, target, start, mid -1)
  # 중간점 값보다 찾고자 하는 값이 크거나 같은 경우
  else:
    return last(array, target, mid + 1, end)

n, x= map(int, input().split()) # 데이터 개수 N, 찾고자 하는 X
array = list(map(int, input().split())) # 전체 데이터 입력

# 값이 x인 데이터의 개수 확인
count = count_by_value(array, x)

# 값이 x인 원소 존재 안하면
if count == 0:
  print(-1)
else:
  print(count)

# bisect
