N ,M = map(int, input().split())

board = []
result = []

for i in range(N):
  board.append(input())


for i in range(N - 7):
  for j in range(M - 7):
    is_it_black = 0
    is_it_white = 0

    for a in range(i, i + 8):
      for b in range(j , j+ 8):
        if (a + b) % 2 == 0:
          # B W B W 순서
          if board[a][b] != 'B':
            is_it_black += 1
          if board[a][b] != 'W':
            is_it_white += 1
        else:
          # W B W B 순서
          if board[a][b] != 'W':
            is_it_white += 1
          if board[a][b] != 'B':
            is_it_black += 1
    result.append(is_it_black)
    result.append(is_it_white)

print(min(result))


