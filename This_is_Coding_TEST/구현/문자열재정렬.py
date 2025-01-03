string = list(input())

str_list = []
numbers = ["0","1","2","3","4","5","6","7","8","9"]
num_list = []
for i in range(len(string)):
  if string[i] in numbers:
    num_list.append(int(string[i]))
  else:
    str_list.append(string[i])

str_list.sort()
result = ""
for i in range(len(str_list)):
  result += str_list[i]

add = sum(num_list)

print(result+str(add))



