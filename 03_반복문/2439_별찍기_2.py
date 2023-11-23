# 오른쪽 정렬 how?
### 4공백 1별
### 3공백 2별

import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

for i in range(1, N + 1):
  print(("*" * i).rjust(N))