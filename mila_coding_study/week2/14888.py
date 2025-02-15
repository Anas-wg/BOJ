N = int(input())

lst = list(map(int, input().split()))

operators = list(map(int, input().split()))

mx = -1e9
mn = 1e9

def dfs(n, temp) : # n : 현재 몇번째 숫자를 계산하였는가, temp : 계산결과 저장 변수
    global mx, mn
    
    # 종료 조건
    if n == N-1:
        mx = max(temp, mx)
        mn = min(temp, mn)
        return
     
    # 하부함수 호출
    if operators[0] != 0 : # 덧셈하는 경우
        operators[0] -= 1
        dfs(n+1, temp + lst[n+1])
        operators[0] += 1 

    if operators[1] != 0 : # 뺄셈하는 경우
        operators[1]-= 1
        dfs(n+1, temp - lst[n+1])
        operators[1] += 1
    
    if operators[2] != 0 : # 곱셈하는 경우
        operators[2] -= 1
        dfs(n+1, temp * lst[n+1])
        operators[2] += 1
    
    if operators[3] != 0 : #나눗셈하는 경우
        operators[3] -= 1
        dfs(n+1, int(temp/lst[n+1])) # int 를 활용하여 실수를 정수화
        operators[3] += 1

dfs(0, lst[0])
print(mx)
print(mn)