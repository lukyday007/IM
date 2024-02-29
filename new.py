def func(i, s):
    global ans
    if i != N and s > M:
        return

    if i == N:
        if s == M:
            ans += 1
        else:
            return
        return


    func(i + 1, s + arr[i])
    func(i + 1, s)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0

    func(0, 0)
