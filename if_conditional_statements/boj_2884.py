# 알람 시계
H, M = map(int, input().split())

# 내 코드
'''
M -= 45

if M < 0:
    H -= 1
    M += 60
    if H < 0:
        H = 23
'''

# 다른 사람 코드
# m이 음수일 경우, m % n 하면 n + m 값이 나온다.
# m이 음수일 경우, m // n 하면 내림 값이 나온다.
H = (H + ((M-45) //60)) % 24
M = (M-45) % 60 

print(H, M)