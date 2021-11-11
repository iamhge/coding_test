# 떡볶이 떡 만들기
'''
<풀이 방법>
  적어도 M만큼의 떡을 얻기 위한 높이의 최댓값이므로 꼭 M이 아니어도 된다.
  자를 수 있는 최대 길이를 end, 최소 길이를 start로 지정한 후, mid 길이만큼 절단했을 때의 결과(tmp)가 target 길이 보다 크거나 같을 경우 result 를 갱신한다.
'''
import sys

input = sys.stdin.readline

def binarySearch(array: list, target: int, start: int, end: int):
    result = 0

    while start <= end:
        mid = (start + end) // 2

        # tmp = (mid 길이로 절단했을 때 잘린 떡들의 길이 합)
        tmp = 0
        for i in array:
            if i > mid:
                tmp += i - mid

        if tmp >= target: # 더 잘라야하거나 최적
            result = mid
            start = mid + 1
        else: # 덜 잘라야 함
            end = mid - 1

    return result

N, M = map(int, input().split())
h = list(map(int, input().split()))
print(binarySearch(h, M, 0, max(h)))