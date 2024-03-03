# 정사각형 방
N = int(input())
rooms = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
mx = 0
'''
2
1 2
3 4
'''

r, c = 0, 0
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
def find_max(y, x, lst):
    global mx

    if lst and rooms[y][x] < lst[-1]:
        return 
    
    # if lst and rooms[y][x] - lst[-1] != 1:
    #     return False
    if lst and rooms[y][x] - lst[-1] == 1:
        lst.append(rooms[y][x])
        mx = max(mx, len(lst))
        print(lst, mx)
    visit[y][x] = 1

    for d in range(4):
        nr = y + dr[d]
        nc = x + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if visit[nr][nc] != 1:
                find_max(nr, nc, lst)
                visit[nr][nc] = 0
                lst.pop()

for r in range(N):
    for c in range(N):
        if rooms[r][c] != N*N:
            find_max(r, c, [rooms[r][c]])

print(mx)