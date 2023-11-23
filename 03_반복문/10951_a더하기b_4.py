import sys
sys.stdin = open("input.txt", "r")
### 종료조건을 how? -> EOF
while True:
  try:
    a, b = map(int, sys.stdin.readline().strip().split())
    print(a + b)
  except:
    break
  