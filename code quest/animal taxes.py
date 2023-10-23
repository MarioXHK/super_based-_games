import sys

#WHO WOULD MAKE A TAX BASED ON THE AMOUNT OF TOTAL ANIMAL LEGS?!

cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    numbers = sys.stdin.readline().rstrip().split(" ")
    for n in range(len(numbers)):
        numbers[n] = int(numbers[n])
    print(numbers[0]*2+(numbers[1]+numbers[2])*4)
    