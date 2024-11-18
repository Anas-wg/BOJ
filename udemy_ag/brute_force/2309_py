import sys
from itertools import combinations


# 입력받기
dwarf_height = []
for i in range(9):
  height = int(input())
  dwarf_height.append(height)

# 조합 활용 
def find_combination (arr, n):
  for comb in combinations(arr, n):
    if sum(comb) == 100:
      return comb

# 오름차순 정렬    
result = list(find_combination(dwarf_height,7))
result.sort()


for i in result:
  print(i)