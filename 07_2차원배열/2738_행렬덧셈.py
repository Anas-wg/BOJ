A, B = [], []

N, M = map(int, input().split())

for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)
for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()

# 어차피 input은 위에서 차례대로 받아오기때문에 또다른 뭔가가 필요한게 아니라
# 그냥 순서대로 받아오면 됨.
