import sys

N = int(sys.stdin.readline().rstrip())
shop = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
customer = list(map(int, sys.stdin.readline().rstrip().split()))

shop.sort()


def binary_search(array, target, start, end):
  if start > end:
    return "no"
  mid = (start + end) // 2
  if array[mid] == target:
    return "yes"
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  else:
    return binary_search(array, target, mid + 1, end)

  
for elems in customer:
  result = binary_search(shop, elems, 0, N - 1)
  print(result, end=" ")

# 집합 자료형 활용
N = int(sys.stdin.readline().rstrip())
# 집합 자료형으로 기록
shop = set(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
customer = list(map(int, sys.stdin.readline().rstrip().split()))

# 단순히 데이터가 있는지 없는지만 확인
for elems in customer:
  if elems in shop:
    print("yes", end=" ")
  else:
    print("no", end=' ')