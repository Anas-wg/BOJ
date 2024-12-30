N, M = map(int, input().split())

def union(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else: 
    parent[a] = b

def find_parent(parent, x):
	if parent[x] != x:
		return find_parent(parent, parent[x])
	return parent[x]

parent = [0] * (N + 1)


for i in range(M):
    op, a, b = map(int,input().split)
    if op == 0:
        union(parent, a, b)
    elif op == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES", end=" ")
        else:
            print("NO", end=" ")
    