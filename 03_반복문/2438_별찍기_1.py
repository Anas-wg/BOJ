import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

for i in range(1, N + 1):
  print("*" * i)