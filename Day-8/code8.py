# Topics Covered:
'''
1. dir, __dict__, help method in Python
2. Use of super() keyword in Python
3. Magic/Dunder methods
4. Method overriding in child class
5. Operator Overloading in Python
6. Types of Inheritance
    a. Single Inheritance
    b. Multiple Inheritance
    c. Multilevel Inheritance
    d. Hierarchical Inheritance
    e. Hybrid Inheritance
'''





# dir, __dict__, help method in Python

# dir:
'''
1. It basically tell about all functions and methods that can be used on the object 'variable'. 
2. All functions of format __func__ are called dunder functions.
'''
variable=(1,4,5,2,33,21)
print(dir(variable))               # prints all possible functions that is possible on tuple
print(variable.__add__)

# __dict__:
class person:
    def __init__(self, n, a):
        self.Name=n
        self.Age=a
person1=person("Aaryan", 19)
person2=person("Arpit", 21)
person3=person("Gaurav", 35)
person4=person("Ritu", 42)

'''Basically '__dict__' return a dictionary in which it takes key as properties of class and value as value to given to that attribute for that particular object on which __dict__ is used.'''
print(person1.__dict__)
# Output: {'Name': 'Aaryan', 'Age': 19 }


# help():
'''
It tells us everything about that objecwhether it is class, string, list, tuple, etc.
It will define each attribute that can be used with that particular object.
'''
# print(help(str))
# print (help(person))


# Use of super() keyword in Python
'''
It is basically use to call the methods or constructors of parent class when inside child class.
'''

# person1 ~ Parent Class
class person1:
    def __init__(self, n, a):
        self.Name=n
        self.Age=a
    def person_info(self):
        print(f"\nName: {self.Name}\nAge: {self.Age}")
# students ~ child class
class students(person1):
    collegeName="AKGEC"
    def __init__(self, n, a, stdID):
        # using super() to call constructor of parent class.
        super().__init__(n, a)
        self.studentID=stdID
    def student_info(self):
        # Using super() to call method of parent class.
        super().person_info()
        print(f"Student ID: {self.studentID}\nCollege Name: {self.collegeName}")

student1=students("Aaryan", 19, 2410007)
student2=students("Arpit", 21, 2310109)
person3=person1("Gaurav", 35)
person4=person1("Ritu", 42)
student1.student_info()
student2.student_info()
person3.person_info()
person4.person_info()


# Magic/Dunder methods
'''
1. Magic/Dunder methods are those methods having '__methodname__' format.
2. We never call these methods directly, but we use it in different way like as shown in Illustration.
'''
'''
1. __init__ - this method gets invoked automatically when instance(object) of a class is created.
'''

# Illustration 1: Use of __len__ method
class Employee:
    Name= "Aaryan"
    def __len__(self):
        i=0
        for letter in self.Name:
            i += 1
        return i
# Creating Instance
emp1=Employee()
'''This is how we call '__len__' method. It has a bit different functionality that's why it is called Magic method.'''
print(len(emp1))

# Illustration 2: Use __str__ method and __repr__ method
''' Basically, '__str__' is used to return something that you want to obtain something when you pass the object name inside any funtion.'''
class Employee1:
    def __init__(self, n):
        self.Name= n
    
    def __len__(self):
        i=0
        for letter in self.Name:
            i += 1
        return i
    def __str__(self):
        return f"Employee Name: {self.Name}"
    def __repr__(self):
        return "Hi buddy, I am repr"
emp2=Employee1("Ajay")
# printing emp2 prints the information that is returned by '__str__' method.
print(str(emp2))
print(repr(emp2))


# Illustration 3: when str is not present in class it fall back to repr when we pass object name into any function.
class Employee1:
    def __init__(self, n):
        self.Name= n
    
    def __len__(self):
        i=0
        for letter in self.Name:
            i += 1
        return i
    # def __str__(self):
    #     return f"Employee Name: {self.Name}"
    def __repr__(self):
        return "Hi buddy, I am repr"
emp2=Employee1("Ajay")
# printing emp2 prints the information that is returned by '__str__' method.
print(emp2)


# Illustration 4: use __call__ method
class AKGEC:
    def __init__(self, N, m, stdID):
        self.Name=N
        self.studentID=stdID
        self.studentMarks=m
    def __call__(self):
        print(f"\nStudent Name: {self.Name}\nStudent ID: {self.studentID}\nStudent Marks: {self.studentMarks}")

student1=AKGEC("Aaryan Kumar", 867, 2410007)
student2=AKGEC("Ajay Kumar", 500, 2410122)
student3=AKGEC("Naresh Kumar", 599, 2410156)
student4=AKGEC("Aditya Singh", 777, 2410100)
# Calling each object name we get to run __call__ method
student1()
student2()
student3()
student4()




# Method overriding in child class 
class shape:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y

class circle(shape):
    def __init__(self, r):
        self.radius=r
        super().__init__(r,r)
    def area(self):
        return 3.14*super().area()

square=shape(5,5)
print(square.area())
circl=circle(5)
print(circl.area())



# Operator Overloading in Python

class vector:
    def __init__(self, i, j, k):
        self.x=i
        self.y=j
        self.z=k
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    '''defining __add__ it tells '+' operator how to behave when two objects are added. It takes two objects as argument. Here one object is self and other one is x'''
    def __add__(self,x):
        return vector(self.x+x.x, self.y+x.y, self.z+x.z)
    
v1=vector(1,2,3)
v2=vector(2,3,4)
print(v1)
print(v2)
'''
1. If in class vector __add__ was not defined then v1+v2 would through error because python don't know these input we are giving are vector and how to add them...
2. So here in this case we have defined how to add two vector that's why we get right output.

NOTE: Notice that to use __add__ defined in class above we are using normal operator here '+' in form 
v1+v2
'''
print(v1+v2)
print(type(v1+v2))
# output: vector
# This is because the fucntion is returning it in 'vector' class format.



# Types of Inheritance

# Type 1: Single Inheritance
class Animal:
    def __init__(self, animal, name):
        self.animal=animal
        self.name=name
    def makeSound(self):
        print(f"I am {self.animal}...My name is {self.name}")
        print("Animallllll Sound....!!!!")
class dog(Animal):
    def __init__(self, name):
        self.name=name
    def makeSound(self):
        print(f"I am a Dog...My name is {self.name}")
        print("Bark....!!!")
a=Animal("Leopard","Frisky")
b=dog("Shadow")
a.makeSound()
b.makeSound()

# Type 2: Multiple Inheritance
class parent1:
    def __init__(self,name):
        self.parent1=name
class parent2:
    def __init__(self,name):
        self.parent2=name
class parent3:
    def __init__(self,name):
        self.parent3=name
class child(parent1,parent2,parent3):
    def __init__(self, childname, name1, name2, name3):
        self.name=childname
        parent1.__init__(self, name1) 
        parent2.__init__(self, name2)  
        parent3.__init__(self, name3)
    def childdetails(self):
        print(f"\nChild Name: {self.name}\nParent 1: {self.parent1}\nParent 2: {self.parent2}\nParent 3: {self.parent3}")
child1=child("Ajay","Kavya","Aaryan","Arpit")
child1.childdetails()


# Method Resolution Order (mro()) 
'''
This tells that when we call a method ...to wo kaha kaha dhoodha jayega to yha pr phle child check hoga, parent1, then parent2, then parent3, to change this order, you have to chnage the argument which you passed while making child class.
'''
print(child.mro())


# Type 3: Multilevel Inheritance
'''When a derived class is derieved from a derived class it is called multilevel inheritance.'''
class Animal:
    def __init__(self, name, animal):
        self.animal=animal
        self.name=name
    def showdetails(self):
        print(f"\nAnimal Name: {self.name}\nAnimal species: {self.animal}")
class Dog(Animal):
    def __init__(self, breed, name):
        Animal.__init__(self, name=name, animal="Dog")
        self.breed=breed
    def showdetails(self):
        Animal.showdetails(self)
        print(f"Animal Breed: {self.breed}")
class GolderRetriever(Dog):
    def __init__(self, name, colour):
        Dog.__init__(self, name=name, breed="Golden Retriever")
        self.colour=colour
    def showdetails(self):
        Dog.showdetails(self)
        print(f"Animal Colour: {self.colour}")

grd=GolderRetriever("Shadow", "Red")
grd.showdetails()
d=Dog("MOTA","Tommy")
d.showdetails()
a=Animal("Jabra", "Leopard")
a.showdetails()

print(GolderRetriever.mro())



# Type 3: Hierarchical Inheritance
'''Forms Hierarchy like structure like:
CEO
    1. SUPER manager1
        a. manager1
        b. manager2
    2. SUPER manager2
        a. manager1
        b. manager2'''

class CEO:
    pass


class SUPERmanager1(CEO):
    pass
class manager1(SUPERmanager1):
    pass
class manager2(SUPERmanager1):
    pass


class SUPERmanager1(CEO):
    pass
class manager1(SUPERmanager1):
    pass
class manager2(SUPERmanager1):
    pass



# Type 4: Hybrid Inheritance
'''Using two or more type Inheritance together is called Hybrid Inheritance. Example given below.'''

class Base_class:
    pass

class derived1(Base_class):
    pass

class derived2(Base_class):
    pass

class derived3(derived1, derived2):
    pass

# End of DAY-8
print("\n\n")
print("THIS IS END OF","#PythonPractice","#Day8",sep="~~")