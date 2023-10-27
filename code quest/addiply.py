import sys


cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    numbers = sys.stdin.readline().rstrip().split(" ")
    a = int(numbers[0])
    b = int(numbers[1])
    print((a+b),(a*b)) 