import sys
# sys.stdin = open("input.txt", "r")
total = int(sys.stdin.readline())
amout = int(sys.stdin.readline())
sum = 0

for i in range(amout):
  a, b = map(int, sys.stdin.readline().split())
  sum += a * b

if sum == total:
  print("Yes")
else:
  print("No")