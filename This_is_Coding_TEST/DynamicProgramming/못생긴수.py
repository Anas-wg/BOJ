N = int(input())

ugly = [0] * N # 못생긴 수 담는 DP 테이블
ugly[0] = 1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음 곱셈값 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 N까지의 못생긴 수 찾기
for l in range(1, N):
  # 가능한 곱셈 결과 중 가장 작은 수 선택
  ugly[1] = min(next2, next3, next5)
  # 인덱스에 따라서 곱셈 결과를 증가
  if ugly[1] == next2:
    i2 += 1
    next2 = ugly[i2] * 2
  if ugly[1] == next3:
    i3 += 1
    next3 = ugly[i3] * 3
  if ugly[1] == next5:
    i5 += 1
    next5 = ugly[i5] * 5

# n번째 못생긴 수 출력
print(ugly[N- 1])