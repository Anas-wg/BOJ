from itertools import combinations
import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())
ability = []

for _ in range(N):
  line = list(map(int, input().split()))
  ability.append(line)

visited = [False for _ in range(N)]
INF = 1e9
res = INF # 팀 능력치 차이의 최솟값을 저장하는 변수

# DFS를 통한 그래프 방문

def DFS(length, index):
  global res
  # 선수 중 절반 돌았다면(나머지는 다른팀)
  if length == N // 2:
    start = 0 # 방문한 선수
    link = 0 # 미방문한 선수
    for i in range(N):
      for j in range(N):
        if visited[i] and visited[j]: # 방문한 선수들(스타트) 능력치 합산
          start += ability[i][j]
        elif not visited[i] and not visited[j]: # 미방문 선수들(링크) 능력치 합산
          link += ability[i][j]
    # res와 팀의 차이를 비교, 둘 중 최솟값으로 설정
    res = min(res, abs(start - link))
    return
  for i in range(index, N):
    if not visited[i]: # 아직 미선택 선수
      visited[i] = True # 스타트 팀 추가
      DFS(length + 1, i + 1) # 다음 선수 선택
      visited[i] = False # 원상태 복귀(백트래킹)

DFS(0, 0)
print(res)
