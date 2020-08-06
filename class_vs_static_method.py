##                          class method vs static method in Python


                                    '''Class Method'''

A class method receives the class as implicit first argument, just like an instance method receives the instance.

Syntax:

class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
fun: function that needs to be converted into a class method
returns: a class method for function.

##NOTE: if self is used in this function,it will give you an error.


1.  A class method is a method which is bound to the class and not the object of the class.

2.  They have the access to the state of the class as it takes a class parameter that points
    to the class and not the object instance.

3.  It can modify a class state that would apply across all the instances of the class.
    For example it can modify a class variable that will be applicable to all the instances.


                                    '''Static Method'''

A static method does not receive an implicit first argument.

Syntax:

class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
        ...
returns: a static method for function fun.

##NOTE: if self or cls is used in this function,it will give you an error.

1. A static method is also a method which is bound to the class and not the object of the class.

2. A static method can’t access or modify class state.

3. It is present in a class because it makes sense for the method to be present in class.



                            '''Class method vs Static Method'''

1. A class method takes cls as first parameter while a static method needs no specific parameters.

2. A class method can access or modify class state while a static method can’t access or modify it.

3. In general, static methods know nothing about class state. They are utility type methods that take
   some parameters and work upon those parameters. On the other hand class methods must have class as parameter.

4. We use @classmethod decorator in python to create a class method and we use @staticmethod decorator
   to create a static method in python.


                               '''When to use what?'''

1. We generally use class method to create factory methods. Factory methods return class object
   ( similar to a constructor ) for different use cases.

2. We generally use static methods to create utility functions.


                        '''How to define a class method and a static method?'''

# Python program to demonstrate 
# use of class method and static method. 
from datetime import date 

class Person: 
	def __init__(self, name, age): 
		self.name = name 
		self.age = age 
	
	# a class method to create a Person object by birth year. 
	@classmethod
	def fromBirthYear(cls, name, year): 
		return cls(name, date.today().year - year) 
	
	# a static method to check if a Person is adult or not. 
	@staticmethod
	def isAdult(age): 
		return age > 18

person1 = Person('mayank', 21) 
person2 = Person.fromBirthYear('mayank', 1996) 

print (person1.age) 
print (person2.age) 

# print the result 
print (Person.isAdult(22))

#Output:
21
21
True

##      @staticmethod
	def isAdult(self): 
		return self.age > 18

'''TypeError: isadult() missing 1 required positional argument: 'self''''

#NOTE: 1. That's why no self or cls is used in static method function
##     2. Similarly,no self is used in class method function



