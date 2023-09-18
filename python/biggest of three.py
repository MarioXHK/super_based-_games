def BiggestOfThree(a: int, b: int, c: int):
    d = 0
    if a > b:
        d = a
        if a < c:
            d = c
    else:
        d = b
        if b < c:
            d = c
    return d
print("Gimme 3 ints pls")
print(BiggestOfThree(int(input("\n")),int(input("\n")),int(input("\n"))))