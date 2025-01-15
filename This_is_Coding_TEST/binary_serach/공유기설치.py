# 집 개수(N)와 공유기 개수(C) 입력
N, C = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보 입력
array = []
for _ in range(N):
  array.append(int(input()))

array.sort() # 이진 탐색 수행 위해 정렬 수행

start = 1 # 가능한 최소 거리(min gap)
end = array[-1] - array[0] # 가능한 최대 거리 (max gap)
result = 0

while (start <= end):
  mid = (start + end) // 2 # 가장 인접한 두 공유기 사이 거리(gap) 의미
  value = array[0]
  count = 1
  # 현재 mid 값 이용하여 공유기 설치
  for i in range(1, N):
    if array[i] >= value + mid:
      value = array[i]
      count += 1
    if count >= C: # C개 이상의 공유기 설치 가능한 경우 거리 증가
      start = mid + 1
      result = mid # 최적의 결과 저장
    else:
      result = mid - 1 # C개 이상 불가한 경우 거리 감소

print(result)
