a, b, c = map(int, input().split())
dice_list = [a, b, c]
dice_list.sort() ### ㅇ[2]가 무조건 큰수


### 같은눈이 나올때
if a == b and b == c:
  prize = 10000 + a * 1000
  print(prize)
### 같은눈이 2개 일때
### 어떻게 같은눈이 2개인 상황을 정의할 것인가 -> a = b or?
### 같은눈 2개를 어떻게 뽑아낼것인가?
elif a == b or a == c or b == c :
  if a == b or a == c:
    standard = a
  if b == c :
    standard = c
  prize = 1000 +  standard * 100
  print(prize)

### 다 다를때
### 3개의 눈의 크기 비교를 어떻게 할 것인가? -> 리스트의 sort 활용
elif a != b and a != c and b != c:
  prize = dice_list[2] * 100
  print(prize)

