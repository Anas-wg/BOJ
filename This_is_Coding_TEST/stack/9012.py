# Stack 활용
import sys

T = int(sys.stdin.readline())

for i in range(T):
  ps = list(sys.stdin.readline().rstrip())
  stack = []
  isVPS = True
  for char in ps:
    if char == '(':
      stack.append(char)
    else:
      if len(stack) > 0:
        stack.pop()
      else: 
        isVPS = False
        break
  
  if len(stack) > 0:
    isVPS = False

  print('YES' if isVPS else 'NO')