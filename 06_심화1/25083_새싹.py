piece_list = list(map(int, input().split()))
chess_piece = [1, 1, 2, 2, 2, 8]
answer_list = []
for i in range(len(piece_list)):
    answer_list.append(chess_piece[i] - piece_list[i])

print(*answer_list)