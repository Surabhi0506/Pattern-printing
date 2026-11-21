for i in range(1,6): #represents number of rows of upper triangle
    for j in range(5 - i): #prints decreasing spaces
        print(" ", end=" ") #prints spaces in same line

    for k in range(2 * i - 1): #prints increasing stars
        print("*", end=" ") #prints stars in same line

    print() #moves to next line

for i in range(4,0,-1): #represents number of rows of lower triangle
    for j in range(5-i): #prints increasing spaces
        print(" ", end=" ") #prints spaces in the same line

    for k in range(2 * i - 1): #prints decreasing stars
        print("*", end = " ") #prints stars in same line
 
    print() #moves to the next line