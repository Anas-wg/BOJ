first_input = input().split()
second_input = input().split()

x = int(first_input[0])
y = int(second_input[0])

if x > 0 :
  if y > 0 :
    print(1)
  else:
    print(4)
if x < 0 :
  if y > 0 :
    print(2)
  else :
      print(3)