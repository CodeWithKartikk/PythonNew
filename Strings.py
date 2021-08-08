# a = "Kartik" or 'Kartik'
# print(a)

'''Multiline strings'''
b = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis error
vero laborum labore cupiditate quos asperiores corrupti! Reiciendis sed 
repellat excepturi voluptatum tenetur accusamus, maxime provident architecto 
voluptatibus soluta officiis! Veniam a sequi tenetur ipsam, sint fugiat 
impedit. Voluptatum eum odit quae incidunt tempore pariatur ut? Numquam 
veritatis veniam harum!"""
  
print(b)

# Strings act as a list
# 0  1  2  3  4  5  6  7  8  9  10
# H  e  l  l  o  _  W  o  r  l  d

a = "Hello World"

for a in "Help

# Concatenation
a = "Kartik "
b = "Gaurav"
print(a+b)

# User = 
# "Thank You for subscribing us Abhishek"

User = input("Enter your name: ")
print("""Thank You for subscribing us
 """ + User)

# 0  1  2  3  4  5  6  7  8  9  10
# H  e  l  l  o  _  W  o  r  l  d

# Slicinig operator stringName[initaal pos : final pos] (0 to 3)

# Slicing 
a = "Hello World"
print(a[0:4])

# Slicing from the start
a = "Hello World"
print(a[:4])

# Slicing to the End
a = "Hello World"
print(a[2:])

#  0   1   2   3   4   5   6   7   8   9   10
#  H   e   l   l   o   _   W   o   r   l   d
# -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1   -------->

b = "Hello World"
print(b[-8:-4])

# Upper Case 
a = "Coding Ninjas paid courses for free"
print(a.upper()) # CODING NINJAS PAID COURSES FOR FREE

# Lower Case
b = "CODING NINJAS PAID COURSES FOR FREE"
print(b.lower())

# Strip 

# c = "     Coding Ninjas paid courses for free --> "
print(c)
s = c.strip()
print(s.strip())
print(s.upper())

Name = "Jartik wants to mearn glutter"
f = Name.replace('J','K') 
print(f)
g = f.replace('m','l')
print(g)
h = g.replace('g','f')
print(h)


# split()

a = "Kartik, Lives, in, Agra"
b = a.split(",")
print(b)
print(type(b))

# Escaping Characters
# String Methods
# Formatting
