# Recursive
def find_parent(parent, x):
  # 루트 노드가 아니라면 찾을때 까지 재귀적 호출
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

# 경로 압축 => 각 원소가 속한 집합과 부모 테이블이 동일
def find_parent_compressed(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합 합치기(UNION)
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력받기
V, E = map(int, input().split())
parent = [0] * (V + 1)

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, V + 1):
  parent[i] = i

# UNION 연산을 각각 수행
for i in range(E):
  A, B = map(int, input().split())
  union_parent(parent, A, B)

# 각 원소가 속한 집합 출력
for i in range(1, V + 1):
  print(find_parent(parent, i), end=' ')

print()

for i in range(1, V + 1):
  print(parent[i], end=' ')
