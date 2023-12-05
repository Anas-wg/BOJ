# UNUCIC 868242
# -> 9 7 9 3 5 3 => 25 + 11 = 36

input = input()
alphabet_list = []
time = 0
for i in range(len(input)):
  alphabet_list.append(input[i])


for i in range(len(alphabet_list)):
  if alphabet_list[i] in ['A', 'B','C']:
    time +=3
  if alphabet_list[i] in ['D', 'E', 'F']:
    time +=4
  if alphabet_list[i] in ['G', 'H', 'I']:
    time +=5
  if alphabet_list[i] in ['J', 'K', 'L']:
    time +=6
  if alphabet_list[i] in ['M', 'N', 'O']:
    time +=7
  if alphabet_list[i] in ['P','Q', 'R', 'S']:
    time +=8
  if alphabet_list[i] in ['T', 'U', 'V']:
    time +=9
  if alphabet_list[i] in ['W','X','Y','Z']:
    time +=10
  
print(time)

