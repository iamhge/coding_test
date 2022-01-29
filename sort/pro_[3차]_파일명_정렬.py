# [3차] 파일명 정렬
import re

def divide(file):
    number = re.findall('\d+', file)[0]
    head = file[:file.index(number)]
    tail = file[file.index(number)+len(number):]
    return head, number, tail, file

def solution(files):
    dividedFiles = []
    for file in files:
        dividedFiles.append(divide(file))
    dividedFiles.sort(key=lambda x: (x[0].upper(), int(x[1])))
    answer = [dividedFiles[i][3] for i in range(len(files))]
    return answer