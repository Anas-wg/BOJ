from collections import deque

def bfs(N, K):
    queue = deque([(N, 0)])  # (현재 위치, 현재 시간)
    visited = [-1] * 100001  # 방문 시간 저장 (-1: 방문X)
    visited[N] = 0  # 시작 위치 방문 처리
    min_time = float('inf')  # 최단 시간 초기값
    count = 0  # 최단 경로의 개수

    while queue:
        pos, time = queue.popleft()

        # 최단 시간보다 크면 탐색 중지
        if time > min_time:
            break
        
        # 동생을 찾은 경우
        if pos == K:
            min_time = time
            count += 1  # 같은 최단 거리라면 방법 개수 증가
            continue

        # 이동 가능한 위치 탐색
        for next_pos in (pos - 1, pos + 1, pos * 2):
            if 0 <= next_pos <= 100000:  # 범위 체크
                # 처음 방문하거나 같은 최단 거리로 방문 가능할 때
                if visited[next_pos] == -1 or visited[next_pos] == time + 1:
                    visited[next_pos] = time + 1  # 방문 시간 저장
                    queue.append((next_pos, time + 1))

    return min_time, count  # 최단 시간, 방법 개수 반환

N, K = map(int, input().split())
time, ways = bfs(N, K)
print(time)
print(ways)
