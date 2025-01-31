# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면 루트 찾을때까지 재귀 호출
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

# 노드의 개수, 간선의 개수 입력
v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

# 부모테이블에서 자기 자신을 부모로 초기화
for i in range(1, v + 1):
  parent[i] = i

# 모든 간선에 대한 정보 입력
for _ in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a ,b))

# cost 순 정렬
edges.sort()

# 각 간선을 모두 돌면서 사이틀 발생 여부 확인
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

