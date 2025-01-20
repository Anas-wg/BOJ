T = int(input())

for tc in range(T):
    N, M = map(int, input().split())  # N: 세로(행), M: 가로(열)
    array = list(map(int, input().split()))

    # DP를 위한 2차원 테이블 생성
    dp = []
    index = 0
    for y in range(N):  # N개의 행
        dp.append(array[index:index + M])
        index += M

    # 다이나믹 프로그래밍 진행
    for x in range(1, M):  # 가로 방향 이동
        for y in range(N):  # 세로 방향 이동
            # 왼쪽 위
            if y == 0:
                left_up = 0
            else:
                left_up = dp[y - 1][x - 1]

            # 왼쪽 아래
            if y == N - 1:
                left_down = 0
            else:
                left_down = dp[y + 1][x - 1]

            # 왼쪽의 경우
            left = dp[y][x - 1]

            # 현재 위치의 최대 금 채굴 값
            dp[y][x] = dp[y][x] + max(left_up, left_down, left)

    # 결과 출력
    result = 0
    for y in range(N):
        result = max(result, dp[y][M - 1])  # 마지막 열에서 최대값 찾기

    print(result)
