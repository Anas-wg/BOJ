N = int(input())

d = [0] * 30001 # 메모이제이션 목적 리스트 초기화

for i in range(2, N + 1):
  # 1 빼는 경우
  d[i] = d[i - 1] + 1
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1)

