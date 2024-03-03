L = int(input())
P = int(input())
cake = [0] * (L + 1)
before = [0] * (P + 1)
after = [0] * (P + 1)
for p in range(1, P + 1):
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        if cake[i] != 0: continue
        cake[i] = p
    before[p] = e - s + 1

for i in range(1, P + 1):
    tmp = 0
    for c in cake:
        if i == c:
            tmp += 1
    after[i] = tmp

print(before.index(max(before)))
print(after.index(max(after)))

