# 붕어 빵 공식 
# ( target_sec / 3초 ) * 2개

# # ver 1
# m, k = map(int, input().split())
# cus = list(map(int, input().split()))

# # m, k = 3, 4
# # cus = [2,2,2]
# idx = 0
# bbang = 0
# res = "possible"
# while idx < len(cus):
#     # 2초 / 3초 * 2 개
#     if (cus[idx] // m) * 2 >= 1:
#         bbang = (cus[idx] // m) * 2 - 1
#     else:
#         res = 'impossible'

#     idx += 1 
# print(res)


# ver 2

# def start():
#     sold_bread = 0
#     for ps in cus:
#         # 공식 
#         made_bread = (ps // m) * k
#         # 빵을 1개 팜
#         sold_bread += 1
#         # 재고 계산 
#         remain = made_bread - sold_bread
#         print(f'ps: {ps}, made_bread : {made_bread}, sold_bread : {sold_bread}')
#         # 재고가 0보다 작으면 실패
#         if remain > 0:
#             return 'impossible'
#     # 실페가 없으면 성공 
#     return 'possible' 

# for tc in range(1, int(input()) + 1):
#     # 손님들이 도착하는 시간
#     cus = list(map(int, input().split()))
#     # m초에 k 개의 빵을 만듦
#     m, k = map(int, input().split())

#     print(f'#{tc} {start()}')


for tc in range(1, int(input()) + 1):
    c, m, k = map(int, input().split())
    cus = list(map(int, input().split()))
    # 정렬되서 입력된다는 보장이 없음 
    cus.sort()
    ans = 'Possible'
    cnt = 0
    for cu in cus:
        cnt += 1
        if cu//m * k < cnt:
            ans = 'Impossible' 
            break

    print(f'#{tc} {ans}')







