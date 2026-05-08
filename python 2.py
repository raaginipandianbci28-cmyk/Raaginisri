main_list = []
MyList1 = []
MyList2 = []
print("Enter 10 integers:")
for i in range(10):
    num = int(input(f"Enter integer {i+1}: "))
    main_list.append(num)
for num in main_list:
    if num % 2 == 0 and num % 3 != 0:
        MyList1.append(num)
    if num % 9 == 0:
        MyList2.append(num)
print("\nMyList1 (Divisible by 2 and not by 3):", MyList1)
print("MyList2 (Multiples of 9):", MyList2)
