##                              Class or Static Variables in Python

The Python approach is simple, it doesn’t require a static keyword.
All variables which are assigned a value in class declaration are class variables.
And variables which are assigned values inside methods are instance variables.


# Python program to show that the variables with a value 
# assigned in class declaration, are class variables 

# Class for Computer Science Student 
class CSStudent: 
	stream = 'cse'				 # Class or static Variable 
	def __init__(self,name,roll): 
		self.name = name		 # Instance or non-static Variable 
		self.roll = roll		 # Instance or non-static Variable 

# Objects of CSStudent class 
a = CSStudent('Geek', 1) 
b = CSStudent('Nerd', 2) 

print(a.stream) # prints "cse" 
print(b.stream) # prints "cse" 
print(a.name) # prints "Geek" 
print(b.name) # prints "Nerd" 
print(a.roll) # prints "1" 
print(b.roll) # prints "2" 

# Class variables can be accessed using class 
# name also 
print(CSStudent.stream) # prints "cse" 


##                                Changing Class Members in Python

We should change class variables using class name only.

# Program to show how to make changes to the 
# class variable in Python 

# Class for Computer Science Student 
class CSStudent: 
	stream = 'cse'	 # Class Variable 
	def __init__(self, name, roll): 
		self.name = name 
		self.roll = roll 

# New object for further implementation 
a = CSStudent("check", 3) 
print ("a.tream =", a.stream) 

# Correct way to change the value of class variable 
CSStudent.stream = "mec"
print ("\nClass variable changes to mec")

# New object for further implementation 
b = CSStudent("carter", 4) 

print ("\nValue of variable steam for each object")
print ("a.stream =", a.stream) 
print ("b.stream =", b.stream) 


To list the attributes of an instance/object, we have two functions:-

1. vars()– This function displays the attribute of an instance in the form of an dictionary.
2. dir()–  This function displays more attributes than vars function,as it is not limited to
           instance. It displays the class attributes as well. It also displays the attributes
           of its ancestor classes.
 
print (vars(a))
print (dir(a))

#Output:
{'name': 'check', 'roll': 3}
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
 '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'roll', 'stream']
