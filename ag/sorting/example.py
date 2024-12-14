arr = [7, 5, 9, 0, 3, 1, 6 ,2, 4, 8]

# 선택 정렬
for i in range(len(arr)):
  min_index = i # 가장 작은 원소의 인덱스
  for j in range(i + 1, len(arr)):
    if arr[min_index] > arr[j]:
      # min_index 번째 원소보다 작은 것 발견시 교체
      min_index = j
  # 스와프
  arr[i], arr[min_index] = arr[min_index], arr[i]

# 삽입 정렬

for i in range(1, len(arr)):
  # i 부터 1까지 감소하여 반복
  for j in range(i, 0, -1):
    if arr[i] < arr[j - 1]: # 한 칸씩 왼쪽으로 이동
      arr[j], arr[j -1] = arr[j -1], arr[j]
    else: # 자신 보다 작은 데이터를 만나면 그 위치에서 Stop
      break

# 퀵정렬 

def quick_sort(array, start, end):
  if start >= end: # 원소 한개인 경우
    return
  pivot = start # 1번째 원소 피벗 지정
  left = start + 1
  right = end
  while left <= right:
    # pivot 보다 큰 데이터 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      right -= 1
    if left > right: # Left, Right 엇갈린 경우
      #Left와 피벗을 교환
      array[left], array[pivot] = array[pivot], array[left]
    else:
      # L,R 이 엇갈리지 않았다면 L, R을 교환
      array[left], array[right] = array[right], array[left]
  # 분할 이후 왼쪽, 오른쪽 부분에서 각각 정렬을 수행
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

# 파이썬 장점 퀵 정렬