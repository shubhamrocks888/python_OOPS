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





 
