cases = int(input())

for i in range(cases):
    numbs = input().split(" ")
    for j in range(len(numbs)):
        numbs[j] = int(numbs[j])
    for f in range(numbs[0]+1):
        for u in range(0,numbs[1]*5+5,5):
            house = (f+u == numbs[2])
            if house:
                break
        if house:
            break
    print(house)