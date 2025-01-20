N = int(input()) # 전체 상담 개수
T = [] # 각 상담 완료시 걸리는 기간
P = [] # 각 상담 완료시 받는 금액

dp = [0] * (N + 1) # DP를 위한 1차원 DP 테이블 초기화
max_value = 0

for _ in range(N):
  x, y = map(int, input().split())
  T.append(x)
  P.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(N -1, -1, -1):
  time = T[i] + i
  # 상담이 기간 안에 끝나는 경우
  if time <= N:
    # 점화식에 맞게, 현재까지의 최고 이익 계산
    dp[i] = max(P[i] + dp[time], max_value)
    max_value = dp[i]
  else: # 상담이 기간 벗어나는 경우
    dp[i] = max_value

print(max_value)