# Module 3 Assignment
# Darren Brown

myfile = open("Question.txt", "r+")

myquestion = myfile.read()

myresponse = input(myquestion)

myfile.write(myresponse)

myfile.close()
