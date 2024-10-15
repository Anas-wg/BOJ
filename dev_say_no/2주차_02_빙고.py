import sys

# 입력받기
bingo_board = []
for i in range(5):
    bingo_board.append(list(map(int, sys.stdin.readline().split())))

mic_call = []
for i in range(5):
    mic_call.append(list(map(int, sys.stdin.readline().split())))

mic_call = sum(mic_call, [])

# X기록용 2차원 배열
record_x = [["O" for j in range(5)] for i in range(5)]

# X 표 기록 함수
def draw_line(arr):
    count = 0
    # 가로줄
    for row in arr:
        if all(elems == 'X' for elems in row):
            count += 1
    # 세로줄
    for col in range(5):
        if all(arr[i][col] == 'X' for i in range(5)):
            count += 1
    # 대각선
    if all(arr[i][i] == 'X' for i in range(5)):
        count += 1
    if all(arr[i][4-i] == 'X' for i in range(5)):
        count += 1

    return count

total_count = 0

# 사회자와 철수 보드를 비교
for called_num in mic_call:
    for i in range(5):
        for j in range(5):
            if bingo_board[i][j] == called_num:
                record_x[i][j] = 'X'
                total_count = draw_line(record_x)
                if total_count >= 3:
                    print(mic_call.index(called_num) + 1)  
                    sys.exit()

