# 자기 방으로 돌아가기

# # ver 1
# for tc in range(1, int(input()) + 1):
#     stu = int(input())
#     corridor = []
#     for _ in range(stu):
#         s, e = map(int, input().split())
#         corridor.append(s)
#         corridor.append(e)
#
#     cnt = 1
#     for i in range(1, len(corridor), 2):
#         if i + 1 >= len(corridor): continue
#         if corridor[i] > corridor[i+1]:
#             cnt += 1
#
#
#     print(f'#{tc} {cnt}')


# ver 2: 지나가면 + 1
# for tc in range(1, int(input()) + 1):
#     student = int(input())
#     cor = [0] * 402
#     for _ in range(student):
#         fro, to = map(int, input().split())
#         cor[fro] += 1
#         cor[to] += 1
#
#     print(f"#{tc} {max(cor)}")

# # ver 3: 항상 작은 숫자 방에서 큰 숫자 방으로 가는 게 아님!!!!!!
# # 10 개 중 9 개 맞음 : 1에서 3으로 갈때와 3 에서 5로 갈 때 딜레이가 없다..?
for tc in range(1, int(input()) + 1):
    student = int(input())
    cor = [0] * 402

    for _ in range(student):
        start, end = map(int, input().split())
        if start > end :
            start, end = end , start

        for i in range(start, end + 1):
            cor[i] += 1

    print(f"#{tc} {max(cor)}")


# ver 4 : 지나가는 복도를 기준으로 접근
# if 짝수 : s -= 1, e -= 1
for tc in range(1, int(input()) + 1):
    student = int(input())
    cor = [0] * 200

    for _ in range(student):
        start, end = map(int, input().split())
        if start > end :
            start, end = end , start

        for i in range((start-1)//2, (end-1)//2 + 1):
            cor[i] += 1

    print(f"#{tc} {max(cor)}")



























