import sys
sys.stdin = open("input.txt","r")
# N, M 받기
N, M = map(int, sys.stdin.readline().split())
basket_list = []
# 길이 N 갖는 바구니 리스트 만들기
for i in range(N):
  basket_list.append(0)
# i, j , k 입력받기
# i번부터 j번 바구니에 k번이 적힌 공을 넣음
# basket_list
for i in range(M):
  i , j , k = map(int, sys.stdin.readline().split())
  for x in range(i , j + 1):
    # 1번의 idx는 0
    basket_list[x - 1] = k


print(*basket_list)
