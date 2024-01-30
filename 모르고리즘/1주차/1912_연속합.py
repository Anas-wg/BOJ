## DP 문제
N = int(input())

arr = list(map(int, input().split()))
print(arr)
dp_sum = [0] * N
dp_sum[0] = arr[0]

# N-1번째까지의 합과 N 번째 값을 비교

for i in range(1, N):
  dp_sum[i] = max(arr[i], arr[i] + dp_sum[i - 1])
  print(dp_sum)

print(max(dp_sum))
  