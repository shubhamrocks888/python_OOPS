##                                    Methods

Function that belongs to a class is called an Method.
All methods require ‘self’ parameter. If you have coded in other OOP language
you can think of ‘self’ as the ‘this’ keyword which is used for the current object.
It unhides the current instance variable.’self’ mostly work like ‘this’.

            '''The self''' :

1.  Class methods must have an extra first parameter in method definition.
2.  We do not give a value for this parameter when we call the method, Python provides it
    If we have a method which takes no arguments, then we still have to have one argument
    – the self. See fun() in above simple example.
3.  this is similar to this pointer in C++ and this reference in Java.


##When we call a method of this object as myobject.method(arg1, arg2), this is automatically
##converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.

    '''myobject.method(arg1, arg2) = MyClass.method(myobject, arg1, arg2)'''

# A Python program to demonstrate working of class methods 
class Vector2d:
     x = 0
     y = 0

     def set(self,x,y):
          self.x = x
          self.y = y

     def output(self):
          print ("bye")

vec = Vector2d()
vec.set(1,2)
print (vec.x,vec.y)
print (Vector2d.x,Vector2d.y)
vec.output()
Vector2d.output(vec)


#Output:
1 2
0 0
bye
bye
