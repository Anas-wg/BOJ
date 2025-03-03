N = int(input())

dp = []

# DP 로 두 번째 줄부터 내려가면서 확인
for i in range(1, N):
  for j in range(i + 1):
    # 왼쪽 위에서 내려오는 경우
    if j == 0:
      up_left = 0
    else:
      up_left = dp[i - 1][j - 1]
    # 바로 위에서 내려오는 경우
    if j == i:
      up = 0
    else:
      up = dp[i - 1][j]
    
    # 최대 합 저장
    dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[N - 1]))