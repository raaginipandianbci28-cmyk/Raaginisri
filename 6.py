for row in range(0,3):
    for column in range(0,):
        if(row==0and column in(1,2,3)):
            print("*",end=" ")
        elif(row in (1,2,4,5)) and (column in (0,4)):
            print("*",end=" ")
        elif(row==6) and (column in (1,2,3)):
            print("*",end=" ")
        else:
            print(' ',end=' ')
    print()
           
        
