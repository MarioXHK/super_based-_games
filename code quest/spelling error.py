import sys


cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    numbers = sys.stdin.readline().rstrip().split(" ")
    knownwords = []
    erroneous = []
    for i in range(int(numbers[0])):
        knownwords.append(sys.stdin.readline().rstrip())
    for j in range(int(numbers[1])):
        erroneous.append(sys.stdin.readline().rstrip())
    for t in range(len(erroneous)):
        wordhits = []
        for f in knownwords:
            wordhits.append(0)
        for h in range(len(erroneous[t])):
            for g in range(len(knownwords)):
                if h >= len(erroneous[t]) or h >= len(knownwords[g]):
                    break
                if erroneous[t][h] == knownwords[g][h]:
                    wordhits[g] += 1
        print(knownwords[wordhits.index(max(wordhits))])
    