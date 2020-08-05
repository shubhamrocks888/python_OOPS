
                        '''Class and Instance Variables (Or attributes)'''
In Python, instance variables are variables whose value is assigned inside
a constructor or method with self.

Class variables are variables whose value is assigned in class.

# Python program to show that the variables with a value 
# assigned in class declaration, are class variables and 
# variables inside methods and constructors are instance 
# variables. 

# Class for Computer Science Student 
class CSStudent: 

	# Class Variable 
	stream = 'cse'			

	# The init method or constructor 
	def __init__(self, roll): 
	
		# Instance Variable	 
		self.roll = roll	 

# Objects of CSStudent class 
a = CSStudent(101) 
b = CSStudent(102) 

print(a.stream) # prints "cse" 
print(b.stream) # prints "cse" 
print(a.roll) # prints 101 

# Class variables can be accessed using class 
# name also 
print(CSStudent.stream) # prints "cse"	 



'''We can define instance variables inside normal methods also.'''

# Python program to show that we can create 
# instance variables inside methods 

# Class for Computer Science Student 
class CSStudent: 
	
	# Class Variable 
	stream = 'cse'	
	
	# The init method or constructor 
	def __init__(self, roll): 
		
		# Instance Variable 
		self.roll = roll			 

	# Adds an instance variable 
	def setAddress(self, address): 
		self.address = address 
	
	# Retrieves instance variable	 
	def getAddress(self):	 
		return self.address 

# Driver Code 
a = CSStudent(101) 
a.setAddress("Noida, UP") 
print(a.getAddress()) 

##Output :
Noida, UP

