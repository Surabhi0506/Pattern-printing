for i in range(5): #represents number of rows
    for j in range(5): #represents number of columns

        if i == 0 or i == 4 or j == 0 or j == 4: #checks for rows and columns which are 0 or 4
            print("*", end=" ") #prints stars in the same line

        else:
            print(" ", end = " ") #prints spaces in the same line
    print() #Moves to the next line