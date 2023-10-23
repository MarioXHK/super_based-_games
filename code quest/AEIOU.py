import sys


cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    line = sys.stdin.readline().rstrip()
        
    count = 0
    for i in range(len(line)):
        if line[i] in {"a","e","i","o","u","A","E","I","O","U"}:
            count += 1

    print(count) 