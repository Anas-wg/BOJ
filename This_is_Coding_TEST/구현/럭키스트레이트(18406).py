N = input()


X = len(N) // 2

list_A = list(map(int, N[:X]))
list_B = list(map(int, N[X:]))

if sum(list_A) == sum(list_B):
  print("LUCKY")
else:
  print("READY")