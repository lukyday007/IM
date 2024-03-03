# magnetic : 스택으로 풀기
import sys
sys.stdin = open('magnetic.txt')
# 위에서 아래로 검사 : 열 검사

# # 열 검사 함수
# def get_zero_cnt(c):
#     cnt = 0
#     # red 자성체를 체크
#     is_red = False

#     for r in range(N):
#         # 1. red 자성체 발견
#         if arr[r][c] == 1:
#             is_red = True
#         # 2. 이전에 red 자성체를 발견, 현재 blue 자성체 발견 + 1
#         elif is_red and arr[r][c] == 2:
#             cnt += 1
#             is_red = False # 갱신

#     return cnt

def get_zero_cnt(col):
    cnt = 0
    isRed = False
    for r in range(N):
        if arr[r][col] == 1:
            isRed = True
        elif arr[r][col] == 2 and isRed:
            cnt += 1
            isRed = False 
    return cnt 

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0 # 열 순회하면서 누적
    for c in range(N):
        total += get_zero_cnt(c)

    print(f'#{tc} {total}')

