for i in range(1, 4): #represents upper 3 rows
    for j in range(i): #prints increasing stars on the left side
        print("*", end=" ") #prints stars in the same line

    for k in range(2 * (3 - i)): #represents decreasing middle spaces
        print(" ", end=" ") #prints spaces in the same line

    for j in range(i): #prints increasing stars on the right side
        print("*", end=" ") #prints stars in the same line
    print() #moves to the next line

for i in range(2, 0, -1): #represents the lower 2 rows

    for j in range(i): #prints decreasing stars on the left side 
        print("*", end=" ") #prints stars in the same line

    for k in range(2 * (3 - i)): #represents increasing middle spaces
        print(" ", end=" ") #prints spaces in the same line
 
    for j in range(i): #prints decreasing stars on the left side
        print("*", end=" ") #prints stars in the same line
    print() #moves to the next line