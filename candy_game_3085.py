# 사탕 게임 
# 초기화 주의!

def count_mx():
    mx = 0
    # 가로열 체크 
    for r in range(N):
        tmp = 1
        for c in range(N - 1):
            if c + 1 >= N: continue
            if board[r][c] != board[r][c + 1]:
                tmp = 1
            else:
                tmp += 1
        mx = max(tmp, mx)
    # 세로열 체크 
    for c in range(N):
        tmp = 1
        for r in range(N - 1):
            if r + 1 >= N: continue
            if board[r][c] != board[r + 1][c]:
                tmp = 1
            else:
                tmp += 1
        mx = max(tmp, mx)

    return mx

dr = [-1,1,0,0]
dc = [0,0,-1,1]

N = int(input())
board = [list(input()) for _ in range(N)]
mxV = 0
for r in range(N):
    for c in range(N):
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if board[r][c] != board[nr][nc]:
                    # 자리 바꾸기 
                    board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
                    tmp = count_mx()
                    mxV = max(tmp, mxV)
                    # 원위치 
                    board[r][c], board[nr][nc] = board[nr][nc], board[r][c]

print(mxV)






