T = int(input())
for i in range(T):
  str = input()
  if len(str) == 1:
    print(str[0]+str[0])
  else:
    print(str[0]+str[-1])
