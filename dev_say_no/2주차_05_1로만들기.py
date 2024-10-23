import sys

# N 입력
N = int(sys.stdin.readline().rstrip())

# DP 초기화
dp = [0 for _ in range(N + 1)]

# 초기값 기록
dp[1] = 0


for i in range(2, N + 1):
  for i in range(2, N + 1):
    # 기본적으로 1을 뺄 때의 경우
    dp[i] = dp[i - 1] + 1
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])

