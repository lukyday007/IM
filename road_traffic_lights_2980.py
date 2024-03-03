# 신호등 주기 : 해당위치 시간 % ( 빨간불 + 초록불 )
# 대기 시간 : 빨간불 - 해당위치 시간 % ( 빨간불 + 초록불 )
# => max( 0, 빨간불 - 해당위치 시간 % ( 빨간불 + 초록불 ) )
# 위의 숫자가 양수이면 대기, 음수이면 그냥 지나감 

T, L = map(int, input().split())

tlights = [list(map(int, input().split())) for _ in range(T)]
time = 0
for i in range(L + 1):
    time += 1
    for j in range(len(tlights)):
        if i == tlights[j][0]:
            tmp = max(0, tlights[j][1] - (time % (tlights[j][1] + tlights[j][2])))
            time += tmp

print(time)











