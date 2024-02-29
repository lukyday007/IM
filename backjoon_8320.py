N = int(input())
ans = 0
for i in range(1, N+1):
    for j in range(i, N+1):
        if i*j <= N:
            ans += 1
print(ans)

# greedy
N = int(input())
ans = N
for i in range(2, N):
    n = N//i - (i-1)
    if n < 1:
        break
    ans += n
print(ans)
