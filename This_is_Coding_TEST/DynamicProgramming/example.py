# 피보나치 수열 재귀만 사용시
def fibo(x):
  if x == 1 or x == 2:
    return 1
  return fibo(x - 1) + fibo(x - 2)

# 피보나치 수열 DP + memoization 사용시 (TOP-DOWN)
d = [0] * 100 # 메모이제이션 목적 리스트 초기화
def fibo_dp(x):
  if x == 1 or x == 2:
    return 2
  # 이미 계산한적이 있다면 그대로 리턴
  if d[x] != 0:
    return d[x]
  # 계산하지 않았다면 피보나치 수열 계산 진행
  d[x] = fibo_dp(x - 1) + fibo_dp(x - 2)
  return d[x]

# 피보나치 수열 DP(Bottom-Up)
# 첫번째 피보나치 수, 두번째 수는 1
d[1] = 1
d[2] = 1
n = 99

# 반복문을 통한 Bottom Up dp 구현
for i in range(3, n +1):
  d[i] = d[i -1] + d[i -2]
