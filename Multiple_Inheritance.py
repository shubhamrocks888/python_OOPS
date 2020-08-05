##                                 MULTIPLE INHERITANCE

# Python example to show working of multiple 
# inheritance 
class Base1(object):
     def __init__(self):
          self.str1 = "Geek1"
          print ("Base1")

class Base2(object):
     def __init__(self):
          self.str2 = "Geek2"
          print ("Base2")

class Derived(Base1, Base2):
     def __init__(self):
          # Calling constructors of Base1
          # and Base2 classes
          Base1.__init__(self)
          Base2.__init__(self)
          print ("Derived")

     def printStrs(self):
          print(self.str1, self.str2) 
		

ob = Derived() 
ob.printStrs() 

#Output:
Base1
Base2
Derived
('Geek1', 'Geek2')



# Python example to show working of multiple 
# inheritance

class Base1:
     def __init__(self,name):
          self.name = name

class Base2:
     def __init__(self,last):
          self.last = last

class Base3(Base1,Base2):

     def __init__(self,name,last):
          Base1.__init__(self,name)
          Base2.__init__(self,last)

b1 = Base1("monty")
b2 = Base2("jain")
b3=Base3("shub","agarwal")
print (b3.name,b3.last)


#Output:
shub agarwal
