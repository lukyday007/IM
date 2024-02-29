# 출력 : 보드 위의 흑돌, 백돌의 개수

# 돌을 둘 수 있는지 없는지 확인
# 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있고,
# 그 때의 상대편의 돌은 자신의 돌로 만들 수 있다.
# 8 방향
dr = [1, 1, 0, -1, -1, -1, 0, 1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def possible(r, c, color, N):
    dir = []
    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != color and board[nr][nc] != 0:
            while 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == 0:
                    break
                if board[nr][nc] == color:
                    dir.append(k)
                    break
                nr += dr[k]
                nc += dc[k]
    return dir

for tc in range(1, int(input()) + 1):
    N, time = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    for r in range(N//2-1, N//2 + 1):
        for c in range(N//2-1, N//2 + 1):
            if r == c:
                board[r][c] = 2
            else:
                board[r][c] = 1

    for _ in range(time):
        row, col, c = map(int, input().split())
        row -= 1
        col -= 1
        dir = possible(row, col, c, N)

        if not dir: continue
        board[row][col] = c
        # print(f'a {a}, b {b}, c: {c}, dir {dir}')
        for d in dir:
            a, b = row, col
            # print(d)
            while 0 <= a < N and 0 <= b < N:
                a += dr[d]
                b += dc[d]
                if board[a][b] == c:
                    break
                board[a][b] = c

    w = 0
    b = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                b += 1
            elif board[r][c] == 2:
                w += 1
    print(f'#{tc}', end=" ")
    print(b, w)









