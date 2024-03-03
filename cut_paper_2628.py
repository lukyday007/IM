# # 종이 자르기 
# # ver 1 
# C, R = map(int, input().split())
# # 0 가로
# row = [0] * R
# ro = []
# # 1 세로
# col = [0] * C
# co = []
# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     if a == 0:
#         row[b] = 1
#     elif a == 1:
#         col[b] = 1
        
# for r in range(1, len(row)):
#     row[r] += row[r - 1]
# for c in range(1, len(col)):
#     col[c] += col[c - 1]

# for i in range(max(row) + 1):
#     cnt = row.count(i)
#     ro.append(cnt)
# for j in range(max(col) + 1):
#     cnt = col.count(j)
#     co.append(cnt)

# mx = 0
# for n in ro:
#     for m in co:
#         mx = max(mx, n*m)

# print(mx)


# ver 2
col, row = map(int, input().split())
N = int(input())

# 리스트 요소 채우기 
rList = [0, row]
cList = [0, col]
for _ in range(N):
    dir, num = map(int, input().split())
    # 가로로 자를 때
    if dir == 0:
        rList.append(num)
    # 세로로 자를 때 
    else:
        cList.append(num)

# 정렬하기 
rList.sort()
cList.sort()

# 행에서 가장 큰 값 구하기 
rmx = 0
for i in range(1, len(rList)):
    if rmx < rList[i] - rList[i-1]:
        rmx = rList[i] - rList[i-1]
# 열에서 가장 큰 값 구하기 
cmx = 0
for i in range(1, len(cList)):
    if cmx < cList[i] - cList[i-1]:
        cmx = cList[i] - cList[i-1]

print(rmx * cmx)
















               