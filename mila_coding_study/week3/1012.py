import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가
input = sys.stdin.readline

# 방향 벡터 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# DFS 탐색 함수
def dfs(x, y, graph, N, M):
    graph[y][x] = 0  # 현재 배추 방문 처리 (0으로 변경)

    for i in range(4):  # 4방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 체크 및 방문 여부 확인
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
            dfs(nx, ny, graph, N, M)  # 재귀적으로 연결된 배추 방문

# 입력 받기
T = int(input().rstrip())  # 테스트 케이스 개수

for _ in range(T):
    M, N, K = map(int, input().split())  # M: 가로(열), N: 세로(행), K: 배추 개수
    graph = [[0] * M for _ in range(N)]  # N x M 크기의 2차원 배열 생성 (세로 x 가로)

    # 배추 위치 입력받기
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1  # 배추 위치 표시

    answer = 0  # 필요한 지렁이 수 (배추 그룹 개수)

    # 모든 좌표를 탐색하며 DFS 수행
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:  # 배추가 있는 경우
                dfs(x, y, graph, N, M)  # DFS로 연결된 배추 그룹 탐색
                answer += 1  # 배추 그룹 개수 증가

    print(answer)  # 테스트 케이스별 정답 출력
