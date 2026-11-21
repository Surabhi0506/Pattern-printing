for i in range(1,6): #represents the number of rows
    for j in range(5-i): #prints decreasing spaces in each row
        print(" ", end=" ") #prints spaces in the same line

    for k in range(i): #controls number of stars in each row
        print("*", end=" ") #prints stars on the same line
    print() #moves to the next line after each row