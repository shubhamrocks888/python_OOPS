##                                    Data hiding

In Python, we use double underscore (Or __) before the attributes name
and those attributes will not be directly visible outside.

class MyClass: 

	# Hidden member of MyClass 
	__hiddenVariable = 0
	
	# A member method that changes 
	# __hiddenVariable 
	def add(self, increment): 
		self.__hiddenVariable += increment 
		print (self.__hiddenVariable) 

# Driver code 
myObject = MyClass()	 
myObject.add(2) 
myObject.add(5) 

# This line causes error 
print (myObject.__hiddenVariable) 

##Output :
'''
2
7
Traceback (most recent call last):
  File "filename.py", line 13, in 
    print (myObject.__hiddenVariable)
AttributeError: MyClass instance has 
no attribute '__hiddenVariable' 
'''

In the above program, we tried to access hidden variable outside the
class using object and it threw an exception.

We can access the value of hidden attribute by a tricky syntax:

# A Python program to demonstrate that hidden 
# members can be accessed outside a class 
class MyClass: 

	# Hidden member of MyClass 
	__hiddenVariable = 10

# Driver code 
myObject = MyClass()	 
print(myObject._MyClass__hiddenVariable) 

##Output :
10


'''
Nothing in Python is truly private; internally, the names of private methods
and attributes are mangled and unmangled on the fly to make them seem inaccessible by their given name.
'''

 
