#thing = input("hi\n")
#count = 0
#for i in range(len(thing)):
#    if thing[i] in ["a","e","i","o","u"]:
#        count += 1


import sys

alphabet = {
    "a": 0,
    "A": 0,
    "b": 1,
    "B": 1,
    "c": 2,
    "C": 2,
    "d": 3,
    "D": 3,
    "e": 4,
    "E": 4,
    "f": 5,
    "F": 5,
    "g": 6,
    "G": 6,
    "h": 7,
    "H": 7,
    "i": 8,
    "I": 8,
    "j": 9,
    "J": 9,
    "k": 10,
    "K": 10,
    "l": 11,
    "L": 11,
    "m": 12,
    "M": 12,
    "n": 13,
    "N": 13,
    "o": 14,
    "O": 14,
    "p": 15,
    "P": 15,
    "q": 16,
    "Q": 16,
    "r": 17,
    "R": 17,
    "s": 18,
    "S": 18,
    "t": 19,
    "T": 19,
    "u": 20,
    "U": 20,
    "v": 21,
    "V": 21,
    "w": 22,
    "W": 22,
    "x": 23,
    "X": 23,
    "y": 24,
    "Y": 24,
    "z": 25,
    "Z": 25,
    " ": 26
}


cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    lettercounterA = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    lettercounterB = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    line = sys.stdin.readline().rstrip()
    print(line)
    line = line.split("|")
        
    for i in range(len(line[0])):
        lettercounterA[alphabet[line[0][i]]] += 1
    for i in range(len(line[1])):
        lettercounterB[alphabet[line[1][i]]] += 1

    print(lettercounterA == lettercounterB) 