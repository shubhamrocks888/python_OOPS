

                                '''The __init__ method'''
The __init__ method is similar to constructors in C++ and Java.
It is run as soon as an object of a class is instantiated.
The method is useful to do any initialization you want to do with your object.

# A Sample class with init method 
class Person: 

	# init method or constructor 
	def __init__(self, name): 
		self.name = name 

	# Sample Method 
	def say_hi(self): 
		print('Hello, my name is', self.name) 

p = Person('Shwetanshu') 
p.say_hi() 

#Output:
Hello, my name is Shwetanshu
