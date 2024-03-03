import sys
sys.stdin = open('frog_jump.txt')

# 개구리가 k번 점프, 밟은 연잎의 모든 숫자의 합은?
# 시작시에 밟고 있는 연잎으 결과에 더하지 않음 
# 연잎 숫자 양수 : 왼 -> 오
#          음수 :  오 -> 왼
# 한 번 뒤로 갔다가 앞으로 -> 직전에 뒤로 간 칸만큼 더 앞으로 점프 
# 범위를 벗어나느 경우 더 이상 점프 X 

# N개의 정수, K번 점프 
N, K = map(int, input().split())
nums = list(map(int, input().split()))
st = []
total = 0
idx = nums[0]   # 2
while K > 0 and idx >= 0 and idx < len(nums):
    total += nums[idx]
    st.append(nums[idx])    # -2
    
    if len(st) > 1 and st[-2] < 0 and st[-1] > 0:
        last = st.pop()
        prev = st.pop()
        idx += nums[last + prev]
        K += 1
        continue
    idx += nums[idx]
    K -= 1
    