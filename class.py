##                                    Classes
Just like every other Object Oriented Programming language Python
supports classes. Let’s look at some points on Python classes.

Classes are created by keyword class.
Attributes are the variables that belong to class.

Attributes are always public and can be accessed using dot (.) operator.
Eg.: Myclass.Myattribute

A sample E.g for classes:

# creates a class named MyClass 
class Myclass:
     number=1
     name = "xyz"

print (Myclass.number)
Myclass.number=2
z = Myclass()
y = Myclass()
print (z.number,y.number)
z.number = 3
print (z.number,y.number)

#Output:
1
2 2
3 2

##                                    Methods

Function that belongs to a class is called an Method.
All methods require ‘self’ parameter. If you have coded in other OOP language
you can think of ‘self’ as the ‘this’ keyword which is used for the current object.
It unhides the current instance variable.’self’ mostly work like ‘this’.

# A Python program to demonstrate working of class methods 
class Vector2d:
     x = 0
     y = 0

     def set(self,x,y):
          self.x = x
          self.y = y

vec = Vector2d()
vec.set(1,2)
print (vec.x,vec.y)
print (Vector2d.x,Vector2d.y)

#Output:
1 2
0 0

