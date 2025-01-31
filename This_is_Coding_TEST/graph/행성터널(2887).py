# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else:
    parent[a] = b

# 노드 개수 입력
N = int(input())
parent = [0] * (N + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트의 최종 비용
edges = []
result = 0

# 부모 테이블 상, 부모를 자기 자신으로 초기화
for i in range(1, N + 1):
  parent[i] = i

x = []
y = []
z = []

# 모든 노드에 대한 죄표 값 입력
for i in range(1, N + 1):
  data = list(map(int, input().split()))
  x.append((data[0], i))
  y.append((data[1], i))
  z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# 인접 노드들로 부터 간선 정보 추출 및 처리
for i in range(N - 1):
  # 비용순 정렬 => 튜플의 첫째 원소 비용으로 설정
  edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
  edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
  edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

# 간선 비용순 정렬
edges.sort()

# 간선 하나씩 확인
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)