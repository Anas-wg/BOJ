import sys
sys.stdin = open("input.txt","r")
# N, M 받기
N, M = map(int, sys.stdin.readline().split())
# 바구니 만들기
basket_list = []
for i in range(N):
  basket_list.append(i+1)

# i,j 활용, i번째 바구니부터 j번째 바구니의 순서를 뒤집기
for a in range(M):
  i, j = map(int, sys.stdin.readline().split())
  med = basket_list[i-1: j]
  med.reverse()
  basket_list[i-1: j] = med

    

print(*basket_list)


