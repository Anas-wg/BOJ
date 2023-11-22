import sys

# sys.stdin = open("input.txt", "r")
number = int(sys.stdin.readline())
add = 0

for i in range(1, number + 1):
  add += i

print(add)