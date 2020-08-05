class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

# Driver Code		 
t = Test(1234, 5678) 
print(t) 

# Output: <__main__.Test instance at 0x7fa079da6710>


##                        Printing Objects

Printing objects gives us information about objects we are working with.
In C++, we can do this by adding a friend ostream& operator <<
(ostream&, const Foobar&) method for the class. In Java, we use toString() method.
In python this can be achieved by using __repr__ or __str__ methods.

class Test:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'repr-->{self.a},{self.b}'

    def __str__(self):
        return f'str--->{self.a},{self.b}'

t = Test(1,2)
print (t)            # This calls __str__() 
print ([t])          # This calls __repr__()

#Output:
str--->1,2
[repr-->1,2]

#Note: if we used return self.a,self.b ,then the O/P will be

TypeError: __str__ returned non-string (type tuple)
