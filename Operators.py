''' 
Author: Kartik Kathuria
Class: Python Operators
Time - 15:23
'''

# Operators are used to perform operations on variables and values

# print(10+5)

'''
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operator
7. Bitise Operator
'''

'''Python Arithmetic Operators'''
# x = 5
# y = 4

# 1. Addition
# print("Addition")
# print(x+y)

# 2. Subtraction
# print("Subtraction")
# print(x-y)

# 3. Multiplication
# print("Multiplication")
# print(x*y)

# 4. Division
# print("Division")
# print(x/y)

# 5. Floor Division
# print("Floor division")
# print(x//y)

# 6. Modulus
# print("Modulus")
# print(x%y)

# 7. Exponentiation
# print("Exponentiation")
# print(x**y)

'''Python Assignment Operators'''
x = 5
# print(x)

# x += 3 
# print(x)

# x -= 3
# print(x)

# x *= 7
# print(x) 

# x /= 5
# print(x)

# x %= 4
# print(x)

# # x //= 3***
# # print(x)

# x **= 3
# print(x)

# x//=5
# print(x)

# x &= 3
# print(x)

# x |= 3 ***
# print(x)

# x ^= 3
# print(x)

# x >>= 3 ***
# print(x)

# x <<= 3 ***
# print(x)

'''Python Comparison Operators'''
# ==, !=, >, <, >=, <=

# == operator
# x = 3
# y = 5

# print(x == y)

# print(x != y)

# print(x > y)

# print(x < y)

# print(x>=y)

# print(x <= y)

''' Python Logical Operators'''
# and -> Returns True if both statements are true
# or -> returns true when if one of the statements is True
# not -> reverse the result

# x = 4
# print(x > 2 and x < 9) 
# print(x < 5 or x >4)
# print(not(x > 2 and x < 9))

''' Python Identity Operators'''

# is -> returns true if both variables are the same object
# is not ->

x = 5
y = 3
z = x
print(x is z)
print(x is y)

'''Mentorship Operators'''

# isNot -> Returns True if both variabess have not same object
print(x is not y)
print(x is not z)

# in -> Returns True if a sequence with a specified value is present in the object 
# not in -> Returns True if a sequence with a specified value is not present in the object 

fruits = ["Apple","Banana"]
print("Banana" in fruits)
print("guava" not in fruits)

'''Bitwise Operators'''
