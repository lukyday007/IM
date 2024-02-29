# # ver 1: 반복사용되는 a 반복변수가 부정확하고 로직상으로 적합하지 않았다 .
# # -> 행 버전, 열 버전으로 분리해서 코드 작성
# board = [[0] * (100+1) for _ in range(100+1)]
# N = int(input())
# def cnt_change(a, b):
#     cnt = 0
#     isOne = False
#     isZero = False
#     for a in range(101):
#         # 0에서 1로
#         if board[a][b] == 1:
#             isOne = True
#         elif isOne and board[a][b] == 0:
#             cnt += 1
#             isOne = False
#         # 1에서 0으로
#         if board[a][b] == 0:
#             isZero = True
#         elif isZero and board[a][b] == 0:
#             cnt += 1
#             isZero = False
#     return cnt
#
# for _ in range(N):
#     a, b = map(int, input().split())
#     for r in range(a, a + 10):
#         for c in range(b, b + 10):
#             board[r][c] = 1
#
# total = 0
# # 위에서 아래로
# for c in range(101):
#     total += cnt_change(c, r)
# # 왼쪽에서 오른쪽으로
# for r in range(101):
#     total += cnt_change(r, c)
# print(total)
#
# # ver 1 - 1 : revised version
# board = [[0] * 101 for _ in range(101)]
# N = int(input())
#
# def cnt_vertical_changes(col):
#     cnt = 0
#     for row in range(1, 101):
#         if board[row][col] != board[row-1][col]:
#             cnt += 1
#     return cnt
#
# def cnt_horizontal_changes(row):
#     cnt = 0
#     for col in range(1, 101):
#         if board[row][col] != board[row][col-1]:
#             cnt += 1
#     return cnt
#
# for _ in range(N):
#     a, b = map(int, input().split())
#     for r in range(a, a + 10):
#         for c in range(b, b + 10):
#             board[r][c] = 1
#
# total = 0
# for c in range(101):
#     total += cnt_vertical_changes(c)
# for r in range(101):
#     total += cnt_horizontal_changes(r)
#
# print(total)

# ver 1 - 2 : revised again
board = [[0] * 101 for _ in range(101)]
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    for r in range(a, a + 10):
        for c in range(b, b + 10):
            board[r][c] = 1

def cnt_transition():
    total = 0
    for r in range(1, 101):
        for c in range(1, 101):
            if board[r][c] != board[r-1][c]:
                total += 1
            if board[r][c] != board[r][c-1]:
                total += 1
    return total

print(cnt_transition())



















