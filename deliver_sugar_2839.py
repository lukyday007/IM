# 설탕 배달 

# ver 1
def get_bag(N):
    for f in range(1001):
        for t in range(1890):
            if 5*f + 3*t == N:
                print(f, t)
                return f + t
    else:
        return -1
    
print(get_bag(int(input())))

# ver 2 : 5kg 봉지 많이 쓰기
def get_bag(N):
    for f in range(N//5, -1, -1):
        t = (N - f * 5)//3
        if 5 * f + 3 * t == N:
            return f + t
    else:
        return -1
    
print(get_bag(int(input())))




