import sys

# 입력 받기
N , K = map(int, sys.stdin.readline().rstrip().split())
coin = []
count = 0

for i in range(N):
  coin.append(int(sys.stdin.readline().rstrip()))

idx = N - 1  # 마지막 동전(가장 큰 동전)부터 시작
while K > 0:
    if coin[idx] <= K:
        count += K // coin[idx]  # 현재 동전으로 사용할 수 있는 최대 개수
        K %= coin[idx]  # 남은 값을 업데이트
    idx -= 1  # 더 작은 동전으로 이동

print(count)



