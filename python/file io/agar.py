import random
number = 23
guessnumber = 0
tries = 0
print("hihi\nI'm thinking of a number from 1 through one quintillion")
while guessnumber != number:
    guessnumber = float(input("Guess\n"))
    print(guessnumber == number)
    tries += 1
    if number < guessnumber:
        print("You're high")
    else:
        print("A new low")
else:
    print("It took you", tries, "tries to guess correctly.")
name = input("Telll me ur name for recording purposes...\n")
myfile = open("C:/Users/671766/Documents/super based games/python/file io/scores.txt", "r")
highscores = myfile.read().split()
myfile.close()

if tries < int(highscores[1]):
    highscores.insert(0,name)
    highscores.insert(1,tries)
elif tries < int(highscores[3]):
    highscores.insert(2,name)
    highscores.insert(3,tries)
elif tries < int(highscores[5]):
    highscores.insert(4,name)
    highscores.insert(5,tries)
elif tries < int(highscores[7]):
    highscores.insert(6,name)
    highscores.insert(7,tries)
elif tries < int(highscores[9]):
    highscores[8] = name
    highscores[9] = tries
while len(highscores) > 10:
    highscores.remove(highscores[10])
print("High scores!:")
for i in range(len(highscores)):
    highscores[i] = str(highscores[i])
    if i % 2 == 1:
        print(highscores[i])
    else:
        print(highscores[i], end = ": ")
newscore = ' '.join(highscores)
myfile = open("C:/Users/671766/Documents/super based games/python/file io/scores.txt", "w")
myfile.write(newscore)
myfile.close()
