hw_list = []
student_list = []

while True:
  try:
    hw_list.append(int(input()))
  except:
    break
hw_list.sort()

for i in range(30):
  student_list.append(i + 1)

# 제출하지 않은 가장 작은 출석번호 찾기
# 1부터 30 들어가있는 리스트와 비교?, len의 차이, 남는 것은?
not_hw = [i for i in student_list if i not in hw_list]
print(not_hw[0])
print(not_hw[1])

