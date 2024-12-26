N = int(input())

array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, N):
  # 지나가는 경우와 이번 창고를 터는 경우중 최대 경우를 저장
  d[i] = max(d[i-1], d[i -2] + array[i])

# index는 0부터 시작하니까 1 차감
print(d[N -1])
