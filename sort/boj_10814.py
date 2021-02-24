# 나이순 정렬
import sys

N = int(sys.stdin.readline().rstrip())
people = []

for _ in range(N):
    people.append(tuple(map(str, sys.stdin.readline().split())))

for age, name in sorted(people, key=lambda person:int(person[0])):
    print(age, name)