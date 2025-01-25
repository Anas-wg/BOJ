# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
  
# 여행지 개수, 여행계획 속한 여행지의 개수 입력받기
N, M = map(int, input().split())
parent = [0] * (N + 1) # 부모 테이블 초기화

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, N + 1):
  parent[i] = i

# union 연산 각각 수행
for i in range(N):
  data = list(map(int, input().split()))
  for j in range(N):
    if data[i][j] == 1: # 연결된 경우 => Union
      union_parent(parent, i + 1, j + 1)

# 여행 계획 입력
plan = list(map(int, input().split()))

result = True
# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(M - 1):
  if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
    result = False

# 여행 계획에 속하는 모든 노두가 서로 연결되어 있는지(루트가 동일한지) 확인
if result:
  print("YES")
else:
  print("NO")