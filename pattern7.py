for i in range(1,6): #represents the number of rows
    for j in range(5-i): #controls number of spaces in each row
        print(" ", end=" ") #prints spaces in same line

    for k in range(2*i-1): #controls number of stars
        print("*", end=" ") #prints stars in same line
    print() #Moves to next line after each row