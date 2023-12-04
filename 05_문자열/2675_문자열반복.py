T = int(input())
new_str = ""
for i in range(T):
  num, str = input().split()
  num = int(num)
  for j in range(len(str)):
    new_str += str[j] * num
  print(new_str)
  new_str = ""

