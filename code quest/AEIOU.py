cases = int(input())

for i in range(cases):
    line = input()
        
    count = 0
    for i in range(len(line)):
        if line[i] in {"a","e","i","o","u","A","E","I","O","U"}:
            count += 1

    print(count) 