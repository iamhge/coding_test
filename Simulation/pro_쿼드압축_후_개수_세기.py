# 쿼드압축 후 개수 세기
from collections import deque

def myZip(arr):
    arrTmp = sum(arr, [])
    
    if sum(arrTmp) == 0:
        return 0
    elif sum(arrTmp) == len(arrTmp):
        return 1
    else:
        return -1

def mySlice(arr, length, row, col):
    result = []
    arrTmp = arr[row[0]:row[1]]
    for i in range(length):
        result.append(arrTmp[i][col[0]:col[1]])
    return result

def solution(arr):
    zero, one = 0, 0
    stack = deque([arr])
    
    while stack:
        array = stack.pop()
        length = len(array)
        
        if length == 1:
            if array[0][0] == 1:
                one += 1
            else:
                zero += 1
            continue
            
        zipped = myZip(array)
        if zipped == 1:
            one += 1
        elif zipped == 0:
            zero += 1
        else:
            myRow = [(None, length//2), (None, length//2), (length//2, None), (length//2, None)]
            myCol = [(None, length//2), (length//2, None), (length//2, None), (None, length//2)]

            for i in range(4):
                stack.append(mySlice(array, length//2, myRow[i], myCol[i]))
    
    return [zero, one]