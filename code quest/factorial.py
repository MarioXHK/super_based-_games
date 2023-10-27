cases = int(input())

for i in range(cases):
    number = int(input())
    for j in range(1,number):
        number = number*j
    print(number) 