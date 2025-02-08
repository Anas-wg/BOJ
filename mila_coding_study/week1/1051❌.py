n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(input()))

# 만들 수 있는 정사각형 한 변의 최대 길이
check = min(n, m)
answer = 0
for i in range(n): # 행을 기준으로 반복
    for j in range(m): # 열을 기준으로 반복
        for k in range(check): # 정사각형 한변의 길이(K + 1)
            # (행 범위, 열 범위 넘지 않는지) and (네개의 꼭짓점이 동일한지)
            if ((i + k) < n) and ((j + k) < m) and (arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]):
                answer = max(answer, (k + 1)**2)
                
print(answer)