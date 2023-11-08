cases = int(input())

for i in range(cases):
    scores = input().split(" ")
    for j in range(len(scores)):
        scores[j] = int(scores[j])
    d = 0
    for k in scores:
        if d == 0:
            d = k
        else:
            if d < k:
                d = k
    print(d)