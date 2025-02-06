import math
from itertools import combinations
A, B = map(int, input().split())

card_list = []
win_percent = 0

# 20장 화투 만들기
for i in range(1, 11):
  card_list.append(i)
  card_list.append(i)

card_list.remove(A)
card_list.remove(B)

combs = list(combinations(card_list, 2))
# 자신이 땡일 경우
if A == B:
  lose_case = 0
  for comb in combs:
    C, D = comb[0] ,comb[1]
    if C == D and C > A:
      lose_case += 1
  win_percent = 1 - (lose_case / len(combs))

# 자신이 끗일 경우
if A != B:
  my_sum = A + B
  if A + B >= 10:
    my_sum -= 10
  win_case = 0

  for comb in combs:
    C, D = comb[0] ,comb[1]
    enemy_sum = C + D
    if C + D >= 10:
      enemy_sum -= 10

    if C != D and my_sum > enemy_sum :
      win_case += 1
  win_percent = win_case /len(combs)


answer = round(win_percent, 3) 
print(format(answer, ".3f"))  