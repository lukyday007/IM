
for tc in range(1, int(input()) + 1):
    arr = [list(input()) for _ in range(5)]
    N = len(arr)
    l = []
    for i in range(N):
        n = len(arr[i])
        l.append(n)
    L = max(l)

    ans = ''
    for r in range(N):
        if l[r] < L:
            for _ in range(L - l[r]):
                arr[r].append('ㄱ')

    for c in range(L):
        for r in range(N):
            if arr[r][c] == 'ㄱ':
                continue
            ans += arr[r][c]
    print(f'#{tc} {ans}')
