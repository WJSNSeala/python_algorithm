import os
import sys

with open("./6_6_data.txt", "r") as fp:
    data = fp.read().splitlines()


def print_board(board):
    print(get_board_size(board))
    for i in board:
        print(i)


def parse_data(input_data):
    data_count = int(input_data[0])
    board_info = []
    data_idx = 0
    for i in range(data_count):
        cur_board = []
        cur_data_info = input_data[1 + data_idx].split(" ")
        for j in range(1, int(cur_data_info[0]) + 1):
            cur_board.append(list(input_data[1 + data_idx + j]))
        data_idx = data_idx + int(cur_data_info[0]) + 1
        board_info.append(cur_board)

    return data_count, board_info


def count_empty_space(board):
    empty_count = 0
    for board_row in board:
        for j in range(len(board_row)):
            if board_row[j] == ".":
                empty_count = empty_count + 1

    return empty_count


def get_board_size(board):
    board_h = len(board)
    board_w = len(board[0])

    return board_h, board_w


board_count, board_data = parse_data(data)

# for i in range(board_count):
#    print(board_data[i])

# print(board_data[0][0][0])
# print(count_empty_space(board_data[0]))

"""
하나 놓고 재귀적으로 처리 => 이러면 블록 놓는 순서에 따라 다른 경우의 수로 취급된다. => 이를 중복 처리 해줘야 함
=> 특정 순서(규칙)에 따라 블록을 놓게하면 순서가 고정되어 같은걸 다르게 세는 경우가 없어진다.

가장 윗 줄 가장 왼쪽을 우선순위로 하여 블록을 놓는다., 해당 지점 기준으로 왼쪽과 위쪽은 모두 블록이 가득 차있다고 생각.

ㅁ    
ㅁㅁ   

ㅁㅁ
ㅁ

ㅁㅁ
  ㅁ 
  
  ㅁ 
ㅁㅁ

"""

cover_type = [  # (dy, dx)
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, -1)]
]


def set(board, y, x, t):
    board_h, board_w = get_board_size(board)
    is_ok = True
    xy_coord = []
    for i in range(3):
        ny = y + cover_type[t][i][0]
        nx = x + cover_type[t][i][1]
        if ny < 0 or ny > board_h or nx < 0 or nx > board_w:
            is_ok = False
        elif board[ny][nx] == "#":  # 이미 차있는 블럭이면
            is_ok = False
        xy_coord.append((ny, nx))

    if is_ok:
        for ny, nx in xy_coord:
            board[ny][nx] = "#"

    return is_ok


def remove(board, y, x, t):
    board_h, board_w = get_board_size(board)
    is_ok = True
    xy_coord = []
    for i in range(3):
        ny = y + cover_type[t][i][0]
        nx = x + cover_type[t][i][1]
        if ny < 0 or ny > board_h or nx < 0 or nx > board_w:
            is_ok = False
        elif board[ny][nx] == ".":  # 이미 차있는 블럭이면
            is_ok = False
        xy_coord.append((ny, nx))

    if is_ok:
        for ny, nx in xy_coord:
            board[ny][nx] = "."

    return is_ok


def cover_count(board):
    # 가장 왼쪽 위 빈칸 찾기
    y, x = -1, -1
    board_h, board_w = get_board_size(board)
    for ny in range(board_h):
        for nx in range(board_w):
            if board[ny][nx] == ".":
                y = ny
                x = nx
                break
        if y != -1:
            break

    # print(y, x)

    if y == -1:  # 블록이 다 채워졌으므로
        return 1

    ret = 0
    for _t in range(len(cover_type)):
        if set(board, y, x, _t):
            ret += cover_count(board)
        remove(board, y, x, _t)

    return ret


print_board(board_data[2])
print(cover_count(board_data[2]))
