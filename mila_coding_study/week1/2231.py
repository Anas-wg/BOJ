N = int(input())

for i in range(1, N + 1):
  num = sum(map(int, str(i)))
  total = i + num
  
  if total == N :
    print(i)
    break
  if i == N :
    print(0)
  

# 더 빠른 풀이
def find_generator(N):
    start = max(1, N - 9 * len(str(N))) 

    for i in range(start, N):
        if i + sum(map(int, str(i))) == N:
            return i
    return 0

N = int(input())
print(find_generator(N))