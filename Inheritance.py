##                                      Inheritance

Inheritance is defined as a way in which a particular class inherits features from its base class.
Base class is also knows as ‘Superclass’ and the class which inherits from the Superclass is knows as ‘Subclass’

Syntax for inheritance: class derived-classname(superclass-name)

# A Python program to demonstrate working of inheritance 
class Person:

     def isperson(self):
          return True

class Employee(Person):
     def isemployee(self):
          return True

p = Person()
e = Employee()
print (p.isperson())
print (e.isperson())
print (e.isemployee())
print (p.isemployee())

#Output:
True
True
True
AttributeError: 'Person' object has no attribute 'isemployee'


# A Python program to demonstrate working of inheritance 
class Pet:

    def __init__(self, name, age):
        self.name = name 
	self.age = age 

# Class Cat inheriting from the class Pet 
class Cat(Pet):

     def __init__(self, name, age):
          # calling the super-class function __init__
          # using the super() function
          super().__init__(name, age) 

thePet = Pet("Pet", 1)
jess = Cat("Jess", 3) 
		
# isinstance() function to check whether a class is 
# inherited from another class
print("Is jess a cat? " +str(isinstance(jess, Cat))) 
print("Is jess a pet? " +str(isinstance(jess, Pet))) 
print("Is the pet a cat? "+str(isinstance(thePet, Cat))) 
print("Is thePet a Pet? " +str(isinstance(thePet, Pet))) 
print(thePet.name,thePet.age)
print (jess.name,jess.age)

class Pet:
    def __init__(self, name, age):
         self.name = name
         self.age = age


# Class Cat inheriting from the class Pet 
class Cat(Pet):
     def __init__(self, name, age):
          # calling the super-class function __init__
          # using the super() function
          super().__init__(name, age) 

thePet = Pet("Pet", 1)
jess = Cat("Jess", 3) 
		
# isinstance() function to check whether a class is 
# inherited from another class
print("Is jess a cat? " +str(isinstance(jess, Cat))) 
print("Is jess a pet? " +str(isinstance(jess, Pet))) 
print("Is the pet a cat? "+str(isinstance(thePet, Cat))) 
print("Is thePet a Pet? " +str(isinstance(thePet, Pet))) 
print(thePet.name,thePet.age)
print (jess.name,jess.age)

#Output:
Is jess a cat? True
Is jess a pet? True
Is the pet a cat? False
Is thePet a Pet? True
Pet 1
Jess 3

##              How to check if a class is subclass of another?
Python provides a function issubclass() that directly tells us if a class is subclass of another class.

# Python example to check if a class is 
# subclass of another 

class Base: 
	pass # Empty Class 

class Derived(Base): 
	pass # Empty Class 

# Driver Code 
print(issubclass(Derived, Base)) 
print(issubclass(Base, Derived)) 

d = Derived() 
b = Base() 

# b is not an instance of Derived 
print(isinstance(b, Derived)) 

# But d is an instance of Base 
print(isinstance(d, Base)) 

#Output:
True
False
False
True


##                       How to access parent members in a subclass?

class Base:

     def __init__(self,x):
          self.x = x

class Derived(Base):

     def __init__(self,x,y):
          Base.x = x
          self.y = y

     def output(self):
          print (Base.x,self.y)

d = Derived(1,2)
d.output()

#Output: 1 2



