# # ver 1 : use while loop
# H, W = map(int, input().split())
# sky = [list(input()) for _ in range(H)]
# board = [[-1] * W for _ in range(H)]

# for h in range(H):
#     for w in range(W):
#         # 구름이 있으면 0으로 표시 
#         if sky[h][w] == 'c':
#             board[h][w] = 0
#         # 보드에 0으로 표시되어 있으면 
#         if board[h][w] == 0:
#             cnt = 1
#             while w + cnt < W:
#                 # 뒤에 구름이 있으면 초기화 
#                 if board[h][w + cnt] == 0:
#                     print('초기화?')
#                     cnt = 1
#                     break
#                 # 걸리는 시간 입력 
#                 board[h][w + cnt] = cnt
#                 cnt += 1
 
# for bo in board:
#     print(*bo)


# ver 2
H, W = map(int, input().split())
arr = [input() for _ in range(H)]
v = [[0] * W for _ in range(H)]

for i in range(H):
    cnt = -1
    for j in range(W):
        if arr[i][j] == "c":
            cnt = 0
        else:
            if cnt >= 0:
                cnt += 1
        v[i][j] = cnt 

for l in v:
    print(*l)









