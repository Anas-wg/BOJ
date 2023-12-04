S = input()
# alphabet 리스트와 일치하는 단어에 입력 단어의 index를 출력,
# 단어가 해당없을시 -1

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str_list = []
for i in range(len(S)):
  str_list .append(S[i])

for i in range(len(alphabet)):
  if alphabet[i] in str_list :
    alphabet[i] = str_list.index(alphabet[i])
  else:
    alphabet[i] = -1

print(*alphabet)