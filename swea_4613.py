# N, M = map(int, input().split())
# flag = [list(input()) for _ in range(N)]

# cnt = []
# for r in range(N):
#     W = 0
#     R = 0
#     B = 0
#     for c in range(M):
#         if flag[r][c] == 'W':
#             W += 1
#         if flag[r][c] == 'R':
#             R += 1
#         if flag[r][c] == 'B':
#             B += 1
#     cnt.append([W, R, B])

# for line in cnt:
#     print(line)

# color = []
# for i in range(len(cnt)):
#     co = 0
#     idx = 0
#     for j in range(len(cnt[i])):
#         if co < cnt[i][j]:
#             co = cnt[i][j]
#             idx = j
#     color.append(idx)
# print(color)


# # 구간 분할 
# N = 7
# arr = [i for i in range(N)]

# # 구간의 시작과 끝 구하기 
# # (0, i) - (i + 1, N - 1)
# # (0, i - 1) - (i, N - 1)

# # i = 0
# # (0, 0) - (1, N - 1)
# # (0, N - 2) - (N - 1, N - 1)

# # 첫 번째 구간의 마지막 위치를 구하기 : 자바, C 언어용 
# for i in range(0, N-2 + 1):
#     print(arr[:i + 1], arr[i + 1 : N])

# print("----------------------")

# # 두 번째 구간의 시작 위치를 기준으로 : 파이썬용 
# for i in range(1, N):
#     print(arr[:i], arr[i:])

# print("----------------------")

# # 3 분할 이상일 때
# # n-1C2
# for i in range(1, N-2 + 1):
#     for j in range(i + 1, N - 1 + 1):
#         print(arr[:i], arr[i:j], arr[j:])

# print("----------------------")

def get_sumOfSubset(k, lst):
    global total, cnt
 
    if total > M:
        return
    if total == M:
        cnt += 1
        return
     
    if k < N:
        used[k] = 1
        total += arr[k]
        lst.append(k)
        get_sumOfSubset(k+1, lst)
        lst.pop()
        total -= arr[k]
        used[k] = 0
        get_sumOfSubset(k+1, lst)

 
 
 
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    used = [0] * N
    total = 0
    cnt = 0
    arr = list(map(int, input().split()))
    get_sumOfSubset(0, [])
    print(f'#{tc} {cnt}')







