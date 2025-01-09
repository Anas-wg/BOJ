import math

N = int(input())
home_list = list(map(int, input().split()))

home_list.sort()
answer = 0

if len(home_list) % 2 != 0:
  answer = home_list[len(home_list) // 2]
else:
  answer = home_list[len(home_list) // 2 - 1]

print(answer)