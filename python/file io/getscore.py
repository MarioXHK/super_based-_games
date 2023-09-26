myfile = open("C:/Users/671766/Documents/super based games/python/file io/scores.txt", "r")
print("Current scores in the file:", myfile.read())
myfile.close()

new_score = input("Enter new scores: ")

myfile = open("C:/Users/671766/Documents/super based games/python/file io/scores.txt", "w")
myfile.write(new_score)
myfile.close()