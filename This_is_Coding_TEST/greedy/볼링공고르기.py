N, M = map(int, input().split())
data = list(map(int, input().split()))

# 1~10 까지 무게 담을 리스트
array = [0] * 11

for x in data:
  # 각 무게에 해당하는 볼링공 개수 카운트
  array[x] += 1

result = 0

for i in range(1, M + 1):
  N -= array[i] # 무개가 i인 볼링공의 개수(A가 선택할 수 있는 개수 제외)
  result += array[i] * N # B가 선택하는 경우와 곱셈

print(result)
