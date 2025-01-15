N = int(input())
num_list = list(map(int, input().split()))


def binary_iteration(array, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == mid:
      return mid # 찾은 경우
    elif array[mid] > mid:
      end = mid - 1 # 중간점보다 찾으려는 값이 작은 경우
    else:
      start = mid + 1 # 중간점보다 찾으려는 값이 큰 경우
  return None

result = binary_iteration(num_list, 0, N - 1)

if result == None:
  print(-1)
else:
  print(result)