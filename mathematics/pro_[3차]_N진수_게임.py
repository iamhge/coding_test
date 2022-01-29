# [3차] N진수 게임
nums = [str(i) for i in range(10)]
nums.extend([chr(65+i) for i in range(6)])

def nNumeral(n, num):
    result = ''
    while num > n:
        result += nums[num % n]
        num //= n
    result += nums[num % n]
    if n <= num:
        result += nums[num // n]
    return result[::-1]

def solution(n, t, m, p):
    answer = ''
    now = 0
    total = ''
    
    while len(total) < m*(t-1) + p:
        total += nNumeral(n, now)
        now += 1
    
    for i in range(p-1, m*(t-1)+p, m):
        answer += total[i]
    
    return answer