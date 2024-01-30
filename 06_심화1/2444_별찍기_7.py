num = int(input())

for i in range(num):
  print(('*'* (2 * i +1)).center(2 *num - 1).rstrip())
  if i == num-1:
    for i in reversed(range(num-1)):
      print(('*'* (2 * i +1)).center(2 *num - 1).rstrip())

