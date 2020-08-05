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


##How to create an empty class?

# An empty class 
class Test: 
	pass





