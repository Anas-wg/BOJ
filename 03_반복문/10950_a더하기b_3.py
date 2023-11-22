import sys
sys.stdin = open("input.txt", "r")
amonut = int(sys.stdin.readline())


for i in range(amonut):
  a, b = map(int, sys.stdin.readline().split())
  print(a + b)