import sys
sys.stdin = open("input.txt", "r")

while True:
  a, b = map(int, sys.stdin.readline().strip().split())
  if a == 0 and b == 0:
    break
  print(a + b)