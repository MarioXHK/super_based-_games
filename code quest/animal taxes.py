cases = int(input())
#WHO WOULD MAKE A TAX BASED ON THE AMOUNT OF TOTAL ANIMAL LEGS?!
for i in range(cases):
    numbers = input().split(" ")
    for n in range(len(numbers)):
        numbers[n] = int(numbers[n])
    print(numbers[0]*2+(numbers[1]+numbers[2])*4)
    