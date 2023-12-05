## 두개의 수를 거꾸로 바꾼다음 비교
A, B = input().split()

## 어떻게 뒤집을까?
reverse_A = A[::-1]
reverse_B = B[::-1]

if reverse_A > reverse_B:
  print(reverse_A)
else:
  print(reverse_B)
