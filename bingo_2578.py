def check(bingo):
    cnt = 0
    cntud = 0
    cntdu = 0
    for r in range(5):
        cntR = 0
        cntC = 0
        
        for c in range(5):
            if bingo[r][c] == "X":
                cntR += 1
            if bingo[c][r] == "X":
                cntC += 1
            if r == c:
                if bingo[r][c] == "X":
                    cntud += 1
            if r + c == 4:
                if bingo[r][c] == "X":
                    cntdu += 1
        
        if cntR == 5:
            cnt += 1
        if cntC == 5:
            cnt += 1
    if cntud == 5:
        cnt += 1
    if cntdu == 5:
        cnt += 1

    return cnt

bingo = [list(map(int, input().split())) for _ in range(5)]
num = []
for _ in range(5):
    num += list(map(int, input().split()))

def get_num():
    for i in range(len(num)):
        for r in range(len(bingo)):
            for c in range(len(bingo[r])):
                if bingo[r][c] == num[i]:
                    bingo[r][c] = "X"
                    res = check(bingo)

                    if res > 2:
                        return i + 1
                        
    return 0
print(get_num())





