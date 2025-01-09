n = int(input())
# 연산 하고자 하는 리스트
data = list(map(int,input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈 
add, sub, mul, div = map(int,input().split())

# 최대, 최소 초기화
min_value = 1e9
max_value = -1e9

# DFS 메서드
def dfs(i, now):
  global min_value, max_value, add, sub, mul, div
  # 모든 연산자 사용한 경우, 최소ㅡ 최대 업데이트
  if i == n:
    min_value = min(min_value, now)
    max_value = max(max_value, now)
  else:
    # 각 연산자에 대해 재귀적 수행
    if add > 0:
      add -= 1
      dfs(i + 1, now + data[i])
      add += 1
    if sub > 0:
      sub -= 1
      dfs(i + 1, now - data[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i + 1, now * data[i])
      mul += 1
    if div > 0:
      div -= 1
      dfs(i +1, int(now / data[i]))
      div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최대, 최소 차례대로 출력
print(max_value)
print(min_value)



