# Topics Covered:
'''
1. Use of seek(), tell() and truncate() function in File Handling in Python
2. Lambda Functions in python ~ One liner functions
3. Use of map() and filter() and reduce() in python
4. Use of 'is' in Python and comparison of 'is' vs. '==' in python
5. OBEJCT ORIENTED PROGRAMMING IN PYTHON [OOPS]
6. Classes and Objects in Python
7. Using Constructor to create Objects in python
'''






# Use of seek(), tell() and truncate() function in File Handling in Python 

# Illustration 1: seek() and tell()
with open('file.txt','r') as f:
    print(type(f))
    f.seek(10)                   # python comes upto 10th byte in that file
    text_reader=f.read(5)        # starts reading after 10th byte i.e. from 11th byte
    print(text_reader)
    print(f.tell())              # It tells your current position within file in bytes

# Illustration 2: truncate()
with open('sample.txt','w') as f:
    f.write('Hello world')
    f.truncate(5)                # It will cut your file content upto your given size



# Lambda Functions in python ~ One liner functions
'''
1. These are anonymous functions ~ don't have any name.
2. It can be of multiple lines
'''
double= lambda x: x*2
cube= lambda x: x*x*x
print(double(2))
print(cube(3))

# NOTE- We can pass function as an argument inside function
def apply(fx,value):
    return 6+fx(value)
print(apply(cube,2))
print(apply(lambda x: x*x*x,2))  # Observe carefully


# Use of map() and filter() ~ built-in funtions

# map():-
'''
1. map() is used when you have to apply same function operation on all items inside list.
2. It return mapped object...you can use explicite type casting to get back list.
3. syntax: map(function, iteratable)
4. Iterable means any iterable object like list, tuple, set, dictionary,etc.
5. These functions take sequence of element as input and return sequence of element as output.
6. These are called higher order funtion because it takes function as its argument.
'''

# Illustration 1: Normal method
def square(x):
    return x*x
list1=[1,2,3,4,5,6,7]
newlist1=[]
for item in list1:
    newlist1.append(square(item))
print(newlist1)

# Illustration 2: map() method
list2=[1,2,3,4,5,6,7,8]
newlist2= list(map(square,list2))      # We can directly use Lambda function here
print(newlist2)

# Illustration 3: lambda function as argument
list3=[1,2,3,4,5,6,7,8,9,10]
newlist3= list(map(lambda x: x*x,list3))
print(newlist3)

# filter():-
'''
1. filter() will keep only those items in list that satisfies the condition.
2. It return filter object...use type casting to convert further
3. syntax: filter(predicting_function, Iterable)
4. It takes those function as argument which returns boolean
5. If function returns 'True' it remains in list otherwise gets filtered.
'''

# Illustration 4: filter() 
def filter_function(a):
    return a>3
filter_list2=list(filter(filter_function,list2))
print(filter_list2)


# reduce() in python ~ not built in ~ need to import
from functools import reduce
def mysum(x,y):
    return x+y
print(reduce(mysum,list2))




# Use of 'is' in Python and comparison of 'is' vs. '==' in python
'''
1. 'is' basically checks for the exact location of the object.
2. '==' just checks whether the value is same or not.
3. Basically 'is' will return True if comparing two immutable objects like strings, tuple, constants.
4. return False when comparing mutable objects.
5. '==' checks just value don't depend on mutable or immutable.
'''

# Illustration 1:
a=(1,2,3)
b=(1,2,3)
c=[1,2,3]
d=[1,2,3]
print(a is b)            # return True because tuple is immutable
print(c is d)            # return False because list is mutable
print(a==b)
print(c==d)



# OBEJCT ORIENTED PROGRAMMING IN PYTHON [OOPS]:

'''NOTE: Take intro about the topic from Video of DAY-#56'''

# Illustration 1: Classes and Objects in Python

# Creating class
class person:
# Creating properties in class:
    Name="default"
    Age="default"
    Occupation="default"
    Gender="default"
    # Creating methods in class: ~ using self is necesaary here
    '''Use of self: It means when you call this method it will info of that object for which it is called.'''
    def info(self):
        print(f"\nName: {self.Name}\nAge: {self.Age}\nGender: {self.Gender}\nOccupation: {self.Occupation}")
# Creating objects:
a=person()
a.Name="Aaryan Kumar"
a.Age="19"
a.Gender="Male"
a.Occupation="Student"

b=person()
b.Name="Arpit Kumar"
b.Age="20"
b.Gender="Male"
b.Occupation="Student"

c=person()
c.Name="Ritu Sah"
c.Age="42"
c.Gender="Female"
c.Occupation="HouseWife"

d=person()
d.Name="Gaurav Chaudhary"
d.Age="35"
d.Gender="Male"
d.Occupation="Software Developer"

a.info()
b.info()
c.info()
d.info()

# Illustration 2: Using Constructor to create Objects in python
''' 
1. A Constructor is a unique function get automatically called/invoked when an object is created of class.
2. It is of two types...Default Constructor...Parametric Constructor
3. IF the constructor do not take any argument (except self ~ self is always required) it is called default otherwise it is parametric.
'''

class person:
    # Creating Constructor ~ using __init()__
    def __init__(self, N, A, G, O):
        self.Name=N
        self.Age=A
        self.Gender=G
        self.Occupation=O
    def info(self):
        print(f"\nName: {self.Name}\nAge: {self.Age}\nGender: {self.Gender}\nOccupation: {self.Occupation}")
e=person("Ajay Kumar", "21", "Male", "Student")
f=person("Naresh Kumar", "19", "Male", "Student")
g=person("Aditya Singh", "20", "Male", "Student")
e.info()
f.info()
g.info()

# End of DAY-6
print("\n\n")
print("THIS IS END OF","#PythonPractice","#Day6",sep="~~")
