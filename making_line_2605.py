# list 의 insert를 쓰면 편함 -> 너무나 pythonic 한 방식 
#                           -> 다른 언어에서는 이렇게 못함 
# # ver 1 
# N = int(input())
# pick = list(map(int, input().split()))
# line = [0] * N


# for i in range(len(pick)):
#     if N - 1 - pick[i] < 0: continue
#     if line[N - 1 - pick[i]] == 0:
#         line[N - 1 - pick[i]] = i + 1
    
#     print(line)


# # ver 2
# N = int(input())
# lst = list(map(int, input().split()))
# ppl = [n for n in range(1, N + 1)]

# for i in range(N):
#     n, p = lst[i], ppl[i]
#     for j in range(i, i - n, - 1): # 이동시킬 자리
#         # print(f"이동시킬 자리 : {j}")
#         ppl[j] = ppl[j - 1]
#         # print(f"자리 이동: {j} -> {j - 1}, ppl : {ppl}")
#     ppl[i - n] = p
#     # print(f"i - n : {i - n}, ppl : {ppl}")
#     # print()

# print(*ppl)

# ver 3
N = int(input())
lst = list(map(int, input().split()))
line = [] 
for i in range(len(lst)):
    line.insert(lst[i], i + 1)
# 뒤집어주기 
line.reverse()
print(*line)

