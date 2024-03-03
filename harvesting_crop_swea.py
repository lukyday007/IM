# # ver 1
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     farm = [list(map(int, list(input())))for _ in range(N)]

#     n = (N + 1)//2
#     # 윗부분
#     total = farm[0][N//2] 
#     # 0, N//2
#     for i in range(1, n): # 0 1 2 
#         c = N//2
#         total += farm[i][c]
#         for j in range(1, i + 1 ): 
#             total += farm[i][c + j] 
#             total += farm[i][c - j]
#     for i in range(n - 2, -1, -1):   # 1 0
#         c = N//2
#         total += farm[N - i - 1][c]
#         for j in range(i , 0, -1):
#             total += farm[N - i - 1][c + j]
#             total += farm[N - i - 1][c - j]

#     print(f'#{tc} {total}')


# # ver 2
# T = int(input())
# for test_case in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int,list(input()))) for _ in range(N)]
 
#     k = 0
#     sum_val = 0
#     for r in range(N):
#         for c in range((N//2)-k,(N//2)+k+1):
#             sum_val += arr[r][c]
#         if r < (N//2): 
#             k += 1
#         else:
#             k -= 1
#     print(f'#{test_case} {sum_val}')   


for tc in range(1, int(input()) + 1):
    steel = list(input())
    st = []
    st.append(steel[0])
    cnt = 0
    for i in range(1, len(steel)):
        if steel[i] =='(':
            st.append(steel[i])

        elif steel[i] == ")":
            st.pop()
            if steel[i-1] == "(":
                cnt += len(st)
            else:
                cnt += 1 
    print(f'#{tc} {cnt}')
        