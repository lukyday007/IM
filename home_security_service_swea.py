from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]  

def bfs(r, c):
    global mx
    visit = [[0] * N for _ in range(N)]
    Q = deque()
    Q.append((r, c))
    # 현재 위치 방문 체크
    visit[r][c] = 1
    house = 0
    # 뻗어나갈 정도 
    K = 0

    if city[r][c] == 1:
        house += 1
    
    while Q:
        x, y = Q.popleft()
        if visit[x][y] == K + 1:
            K = visit[x][y]
            cost = K * (K - 1) * (K - 1)
            if cost <= M * house:
                mx = max(mx, house )              

        for d in range(4):
            nr = x + dr[d]
            nc = y + dc[d]

            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visit[nr][nc] != 0:
                continue

            visit[nr][nc] = visit[x][y] + 1

            for line in visit:
                print(*line)
            print()
            
            if city[nr][nc] == 1:
                house += 1
            
            Q.append((nr, nc))

# N 도시크기 M 집마다 지불할 비용 
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
mx = 0
for r in range(N):
    for c in range(N):
        bfs(r, c)

print(mx)
     





