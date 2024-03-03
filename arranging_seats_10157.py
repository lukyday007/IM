
# # ver 1 : 시간초과 
# R, C  = map(int, input().split())
# num = int(input())

# if num > R * C:
#     print(0)
# else:
#     board = [[0] * C for _ in range(R)]
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     r, c = 0, 0
#     nr, nc = 0, 0
#     d = 0
#     cnt = 1
#     board[0][0] = cnt
#     while any(0 in row for row in board):
#         r, c = r + dr[d], c + dc[d]
#         # 범위 체크
#         if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != 0:
#             # 범위를 벗어나면 아까 저장했던 좌표를 끌어와서 사용 
#             r, c = nr, nc 
#             d = (d + 1) % 4
#             continue
#         # 빈 번호 체크 -> 없으면 번호 채우기 
#         cnt += 1
#         board[r][c] = cnt
#         # 좌표가 범위 벗어날 때 미리 저장할 좌표
#         nr, nc = r, c

#     for r in range(len(board)):
#         for c in range(len(board[r])):
#             if board[r][c] == num:
#                 print(r + 1, c + 1)


# ver 2 : 칸을 다 채울 필요가 없음!!
R, C  = map(int, input().split())
num = int(input())

if num > R * C:
    print(0)
else:
    board = [[0] * C for _ in range(R)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c = 0, 0
    nr, nc = 0, 0
    d = 0
    cnt = 1
    board[0][0] = cnt
    # 입력한 숫자까지만 채워넣기!
    while cnt != num:
        r, c = r + dr[d], c + dc[d]
        # 범위 체크
        if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != 0:
            # 범위를 벗어나면 아까 저장했던 좌표를 끌어와서 사용 
            r, c = nr, nc 
            d = (d + 1) % 4
            continue
        # 빈 번호 체크 -> 없으면 번호 채우기
        cnt += 1
        if cnt == num:
            break
        board[r][c] = cnt
        # 좌표가 범위 벗어날 때 미리 저장할 좌표
        nr, nc = r, c

    print(r + 1, c + 1)



