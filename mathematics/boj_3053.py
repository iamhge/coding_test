import sys

PI = 3.14159265359

R = int(sys.stdin.readline().rstrip())

euclidean = PI * R * R
taxi = 0.5 * (2*R)**2 

print(euclidean)
print(taxi)