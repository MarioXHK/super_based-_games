cases = int(input())

for i in range(cases):
    line = input()

    line = line.split(" ")

    print(int(line[0])+int(line[1]),int(line[0])*int(line[1])) 