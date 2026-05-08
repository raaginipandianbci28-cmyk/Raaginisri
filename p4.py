for row in range(0,7):
    for column in range(0,5):
        if(row==0and column in(1,2,3)):
            print("*",end=" ")
        elif(row in (1,2,3,4,5,6)) and (column in (0,4)):
            print("*",end=" ")
        elif(row==3) and (column in (1,2,3)):
            print("*",end=" ")
        else:
            print(' ',end=' ')
    print()
           
        
