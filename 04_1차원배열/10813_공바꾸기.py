import sys
sys.stdin = open("input.txt","r")
# N, M 받기
N, M = map(int, sys.stdin.readline().split())
basket_list = []
# 바구니리스트 생성
for x in range(N):
  basket_list.append(x + 1)

# i,j 받기
for y in range(M):
  i ,j = map(int, sys.stdin.readline().split())
  # i번 바구니와 j번 바구니의 공 바꾸기
  basket_list[i - 1],basket_list[j - 1] = basket_list[j - 1],basket_list[i -1]

print(*basket_list)
