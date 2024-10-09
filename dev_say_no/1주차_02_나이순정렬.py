import sys

arr = []
N = int(input())

for i in range(N):
  age, name = sys.stdin.readline().rstrip().split(' ')
  arr.append([int(age), name])

arr.sort(key= lambda x: x[0])

for i in range(len(arr)):
  print(*arr[i])