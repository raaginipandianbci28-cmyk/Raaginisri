mylist =["4","4","3","3","1","10"]
mylist =list(dict.fromkeys(mylist))
print(mylist)



my_list =  [1,2,3,4]
c1,c2,c3= clone_list(my_list)
print("Original list :", my_list)
print("Copy using slicing:", c1)
print("Copy using list():", c2)
print("Copy using copy():",c3)
