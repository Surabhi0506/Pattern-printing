for i in range(5,0,-1): #represents number of rows
    for j in range(5-i): #prints increasing spaces
        print(" ", end=" ") 

    for k in range(2 * i - 1): #prints decreasing stars
        print("*", end= " ") #prints stars in the same line
    print() #moves to next line