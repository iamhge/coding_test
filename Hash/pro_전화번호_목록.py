# 전화번호 목록
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
        else:
            continue
    return True

# 다른 사람 풀이
'''
해시를 이용한 정석적인 풀이 방법.
'''
'''
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
'''
# 실패
# 시간 초과
'''
def solution(phone_book):
    phone_book.sort(key = len)
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return True
'''
'''
def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if len(phone_book[i]) <= len(phone_book[j]):
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    return False
            else:
                if phone_book[j] == phone_book[i][:len(phone_book[j])]:
                    return False
    return True
'''