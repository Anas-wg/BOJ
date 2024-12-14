N , M = map(int, input().split())

ans_list = []

for i in range(N):
  num = list(map(int, input().split()))
  min_elem = min(num)
  ans_list.append(min_elem)

print(max(ans_list))