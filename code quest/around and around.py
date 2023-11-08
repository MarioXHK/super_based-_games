cases = int(input())

for i in range(cases):
    Ecirc = 40075
    diam = Ecirc/3.14
    altitude = int(input())
    diam += altitude*2
    Ecirc = diam*3.14
    print(Ecirc) 