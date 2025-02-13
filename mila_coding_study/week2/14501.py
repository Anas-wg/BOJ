N = int(input())
timeTable = [list(map(int, input().split())) for _ in range(N)]

def solve(i):
    if i>=N: # 퇴사일 이후 종료시
        return 0
    ret = 0
    if i+timeTable[i][0]<=N:
        # i번째 상담을 끝낸 후 최대 보상
        ret = solve(i+timeTable[i][0])+timeTable[i][1]
    # 상담을 하지 않고, 그냥 다음날로 넘어가는 경우
    ret = max(ret,solve(i+1))
    return ret

print(solve(0))


# DP 방식
N = int(input())
TP = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1,-1,-1):
    if i+TP[i][0]>N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max (dp[i+1],dp[i+TP[i][0]]+TP[i][1])
print(dp[0])