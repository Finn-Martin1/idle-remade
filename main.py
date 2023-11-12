
import os
loop = True

#opens the file to program in
filename = input("Filename: ")
filename += ".py"
file = open(filename,"a")
while loop:
    user_input = input(">>> ")

    if user_input == "help":
        print("quit - quit shell")
        print("clear - clear shell")
        print("run - run the code")
        print("print - show the code already written")
        print("help - show this message")
        print("newfile - create a new file")
        print("changefile - change the file you are working on")
        print("deletefile - delete a file")
    
    if user_input == "quit":
        loop = False
       
    if user_input == "new file":
        file.close()
        filename = input("Filename: ")
        filename += ".py"
        file = open(filename,"a")
    
    if user_input == "change file":
        file.close()
        filename = input("Filename: ")
        filename += ".py"
        file = open(filename,"a")
   
    if user_input == "delete file":
        closefile = input("what file to delete: ")
        os.remove(closefile)
    
    if user_input == "clear":
        os.remove(filename)
        file = open(filename,"a")

    if user_input == "print":
        file.close()
        file = open(filename,"r")
        print(file.read())
        file.close()
        file = open(filename,"a")

    if user_input == "run":
        file.close()
        exec(open(filename).read())
        file = open(filename,"a")

    if user_input != "quit" and user_input != "clear" and user_input != "run" and user_input != "print" and user_input != "help" and user_input != "new file" and user_input != "change file" and user_input != "delete file":
        file.write(user_input)
        file.write("\n")
    