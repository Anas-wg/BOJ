# 대소문자 구분 없으니 대문자 화
word = input().upper()
# 집합으로 만들어서 중복 X, 
# set 함수는 mutation X
word_list = list(set(word))

cnt = []
for i in word_list:
  # count 메서드 -> 문자열내 특정 문자열 개수 구함
  count = word.count
  cnt.append(count(i))

print(cnt)
if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])

