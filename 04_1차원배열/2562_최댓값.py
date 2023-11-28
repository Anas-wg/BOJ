## 1. 입력받을 리스트생성
input_list = []
while True:
  try:
    input_list.append(input())
  except:
    break

## 정수형으로 변환, 원본은 변화 없이
int_list = list(map(int, input_list))
int_list.sort()
## 최댓값
print(int_list[len(int_list)-1])
## 최댓값이 입력리스트에서 몇번째인가?
for i in range(len(input_list)):
  if int_list[len(int_list)-1] == int(input_list[i]):
    print(i + 1)
