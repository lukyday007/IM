# 줄세우기 10431
# # ver 1
# N = int(input())
# for _ in range(N):
#     lst = list(map(int, input().split()))
#     num, line = lst[0], lst[1:]

#     cnt = 0
#     for i in range(1, len(line)):
#         for j in range(i, -1, -1):
#             if line[i] < line[j]:
#                 cnt += 1
#     print(num, cnt)

# ver 2
N = int(input())
for _ in range(N):
    lst = list(map(int, input().split()))
    num, line = lst[0], lst[1:]

    cnt = 0
    for i in range(1, len(line)):
        for j in range(i):
            if line[i] < line[j]:
                cnt += 1
    print(num, cnt)