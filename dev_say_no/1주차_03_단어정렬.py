import sys

word_list = []
# 입력받기
N = int(input())
for i in range (N) :
  word = sys.stdin.readline().rstrip()
  word_list.append(word)

# 중복제거
word_list = list(set(word_list))

# sort 함수 활용
word_list.sort() 
word_list.sort(key= lambda x: len(x))

for i in word_list:
  print(i)