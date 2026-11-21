for i in range(1,6): #represents number of rows
    for j in range(1, i+1): #represents number of columns
        if j == 1 or j == i or i == 5: #checks in the rows and column is 1 or 5 or if j is equal to j
            print("*", end = " ") #prints stars in the same line

        else:
            print(" ", end=" ") #prints spaces in the same line
 
    print() #moves to next line 