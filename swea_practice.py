# NxN 2차 배열에서
# 항상 현재 위치(r,c)에서
# 오른쪽(r,c+1) 또는 아래(r+1, c) 방향 중 선택
# 마지막은 (N-1, N-1)에 도착한 경우
N = 3
arr = [[0] * N for _ in range(N)]
cnt = 0 
def find_path(r, c): # (r, c) 현재 위치
    global cnt
    arr[r][c] = 1
    if r == N-1 and c == N-1:
        cnt += 1
        for line in arr:
            print(*line)
        print('----------------------')
        return

    # 길을 계속 갑시다.
    # 두가지 선택지를 각각 한번씩 해보는거다....
    # 오른쪽(r, c+1)로
    if c + 1 < N:
        find_path(r, c+1)
    # 아래(r+1, c)
    if r + 1 < N:
        find_path(r+1, c)

    arr[r][c] = 0

# find_path(0, 0)
# print('모든 경로수 = ', cnt)


# 최대 상금 
'''
3
123 1
2737 1
32888 2
'''

def find_max(k):
    global ans
    val = int(''.join(map(str, num)))

    if val in used[k]: return 
    used[k].add(val)

    if k == change:
        ans = max(ans, val)
    else:
        for i in range(N - 1):
            for j in range(i + 1, N):
                num[i], num[j] = num[j], num[i]
                find_max(k + 1)
                num[i], num[j] = num[j], num[i]
    
for tc in range(1, int(input()) + 1):
    num, change = input().split()
    num = list(map(str, num))
    N = len(num)
    change = int(change)
    used = [set() for _ in range(change + 1)]
    ans = 0

    find_max(0)
    print(f'#{tc} {ans}')












