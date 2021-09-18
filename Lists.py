'''
Author- Kartik Kathuria
Date- 18-09-2021
Time- 14:36 p.m. (Noon)
Topic- Lists in Python
'''
#            0         1         2           3         4        5
myList = ["Kartik","Abhishek","Prerita","Tanushka","Apoorva","Ashish"] # Sequential order
myList[0] = "Aman"
print(myList)

# Change/Modify 
# add, remove, change items in a list after creation

'''List Length'''
a = len(myList) 
print(a)

''' list datatypes '''
list1 = ['apple',"banana","guava"]
list2 = [1,2,3,4,5]
list3 = [True, False, True, False]

'''type() function'''
print(type(list1))

# list() Constructor
# It is also possible to use the list constructor() when creating a new list 

thisList = list(("Apple","Banana","cherry"))
print(thisList)
print(type(thisList))

'''
Arrays
 1. List -> []
 2. Tuple -> ()
 3. Set -> {}
 4. Dictionary -> {} 
'''
