# Topics Covered:
'''
1. Decorators in Python
2. Getter and Setter in OOPS in Python
3. Inheritance in Python
4. Access Modifiers in Python and Name Mangling concept in private access modifier
5. Making Static method inside class
6. Difference between Instance Variables and Class Variables
7. Class Methods in Python
8. Class Method as alternative constructor
'''






# Decorators in Python
'''Modifies the existing function() by taking function (fx) as argument and returning modified function (mfx) '''

def greet(fx):
    def mfx():
        print ('Good Morning')
        fx()
        print('Thanks for using this Function')
    return mfx

# Illustration 1: To use the Decorators ~ By using this method the function will get decorated everytime it is called.
@greet                  
def hello():
    print('Hello World')
hello()

# Illustration 2: This is used when you want to decorate at some places where it is necessary
def bye():
    print('Bye World')
greet(bye)()

# Illustration 3: When function using decorator have arguments:
def greethello(fx):
    def mfx(*args, **kwargs):
        print ('Good Morning')
        fx(*args, **kwargs)
        print('Thanks for using this Function')
    return mfx

@greethello
def sum (a,b):
    print (a+b)

sum (6,7)

# Illustration 4: Can be called this way also
def greethello(fx):
    def mfx(*args, **kwargs):
        print ('Good Morning')
        fx(*args, **kwargs)
        print('Thanks for using this Function')
    return mfx


def sum (a,b):
    print (a+b)

greethello(sum)(6,7)



# Getter and Setter in OOPS in Python
'''
GETTER: It is basically a 'method' in class but act as 'property'
SETTER: To manually change the value of Getter...Setter is used...It can be aplied only to method that is Acting as getter.
'''
class AKGEC:
    def __init__(self, N, m, stdID):
        self.Name=N
        self.studentID=stdID
        self.studentMarks=m
    def stdinfo(self):
        print(f"\nStudent Name: {self.Name}\nStudent ID: {self.studentID}\nStudent Percentage: {self.percentage}\nStudent Marks: {self.studentMarks}")
    # creating a getter ~ writing @property is necessary to create a getter
    @property
    def percentage(self):
        return (self.studentMarks/9)
    # creating a setter ~ can only be applied to percentage here ~ only applied to a getter
    @percentage.setter
    def percentage(self, newValue):
        self.studentMarks=newValue*9
student1=AKGEC("Aaryan Kumar", 867, 2410007)
student2=AKGEC("Ajay Kumar", 500, 2410122)
student3=AKGEC("Naresh Kumar", 599, 2410156)
student4=AKGEC("Aditya Singh", 777, 2410100)
student1.stdinfo()
student2.stdinfo()
student3.stdinfo()
student4.stdinfo()

student1.percentage=99
student1.stdinfo()



# Inheritance in Python
'''
Inheritance are of four types:-
1. Single Inheritance
2. Multi Inheritance
3. Multilevel Inheritance
4. Hybrid Inheritance
'''

# Illustration 1:
class AKGEC_1(AKGEC):
    def showlanguage(self):
        print(f"\nStudent Name: {self.Name}\nStudent ID: {self.studentID}\nStudent Percentage: {self.percentage}\nStudent Marks: {self.studentMarks}\nLanguage: Python")

student5=AKGEC_1("Mahima Upadhyay", 666, 2010100)
student5.showlanguage()
student1=AKGEC_1("Aaryan Kumar", 867, 2410007)
student1.showlanguage()



# Access Modifiers in Python
'''
It is of 3 types:
1. Public Access Modifiers
2. Private Access Modifiers
3. Protected Access Modifiers

NOTE: Actually there is nothing like Public, Private and Protected in Python but it is used INDIRECTLY
'''
class account_number:
    def __init__(self, accno):
        # Creating Private ~ by giving '__' as prefix of variable...It is indicated that variable is private and cannot be accessed directly 
        self.__accountNumber=accno

obj=account_number(89697410004545)
# The code below will throw error because the variable is private and cannot be accessed directly.
# print(obj.accountNumber)
# However, It it can accessed indirectly by using method given below ~ using '_ClassName__VariableName'
print(obj._account_number__accountNumber) 
# This format is called 'name mangling method'
'''Name Mangling is a method in python use to prevent accidental changes in attributes of classes or subclasses'''
print(obj.__dir__())      # This give me all function that can be runned on 'obj'


class student:
    def __init__(self, name):
        # Creating Protected Access modifier ~ using '_' before variable name.
        self._name=name
class studentAKGEC(student):
    def info(self):
        print(f"My name is {self._name}")
student11=studentAKGEC("Aaryan Kumar")
student11.info()
'''
NOTE: Basically, Protected can be accessed by only the onjects of that class or subclass.
Every Access Modifier except 'private' can be accessed normaly while in 'private' Name Mangling concept is used to access.
'''


# Making Static method inside class ~ It does not take self argument
class math:
    # When creating a object ...arguments in constructor is required to be passed.
    def __init__(self, num):
        self.num=num
    def showDetails(self):
        print(f"The number is {self.num}")
    # When you call this method on any object you have to pass the argument 'n'
    def addtonum(self,n):
        self.num+=n
    # Creating Static method ~ using @staticmethod decorator
    @staticmethod
    def add(a,b):
        return a+b
object=math(32)
print(object.num)
object.addtonum(32)
print(object.num)
''' 
1. Static methods can be called by using either 'class name' or using 'object'.
2. It acts like Normal function but is placed inside class. It is used normally like other functions
3. It is created when you want that function or method to be shipped along with the class to user of the code.
'''
# Using Static Method
result1=math.add(41,19)
print(result1)
result2=object.add(21,19)
print(result2)


# Method 1: Normally calling showDetails()
object.showDetails()
# Method 2: showDetails() can also be called like ~ Actually the 'method 1' get converted into method 2 and object is passed as an argument, so putting 'self' as argument is necessary to make methods inside class.
math.showDetails(object)


# Difference between Instance Variables and Class Variables
class studentAKG:
    # These are the class Variable.
    collegeName="AKGEC"
    # Initialisation is important
    NoOfStudents=0
    def __init__(self, name, sec, stdID):
        # These are instance Variable ~ can be changed at different objects.
        self.Name=name
        self.Section=sec
        self.StudentID=stdID
        # Initialisation of NoOfStudents is important
        studentAKG.NoOfStudents += 1
    def details(self):
        print(f"\nName: {self.Name}\nSection: {self.Section}\nStudent ID: {self.StudentID}\nCollege: {self.collegeName}\nNo. of students: {self.NoOfStudents}")
student101=studentAKG("Aaryan Kumar", "S-1", 2410007)
student101.details()
student102=studentAKG("Ajay Kumar", "S-1", 2410123)
student102.details()
student103=studentAKG("Naresh Kumar", "S-1", 2410190)
student103.details()
student104=studentAKG("Aditya Singh", "S-1", 2410001)
student104.details()




# Instance variable can be changed manually
student102.Section="S-2"

# Class variable can be changed manually for any individual object while for rest of the objects The class Variable remains same
student103.collegeName="IMSEC"  


student101.details()
student102.details()
student103.details()
student104.details()

# To change the whole class variable directly 
studentAKG.collegeName="ABES EC"

student101.details()
student102.details()
student103.details()
student104.details()



# Class Methods in Python 

# Illustration 1: Without class method:
class studentAKG:
    collegeName="AKGEC"
    NoOfStudents=0
    def __init__(self, name, sec, stdID):
        self.Name=name
        self.Section=sec
        self.StudentID=stdID
        studentAKG.NoOfStudents += 1
    # NOT A Class Method creation ~ It is changing only for particular instance not globally [NOTE]
    '''Yha pe by-default isko phela argument as a object milta h...also we can write anything instead of self, it will take object only as it's first argument.'''
    def changecollegeName(MeriMarzi, new_college):
        MeriMarzi.collegeName=new_college
    def details(self):
        print(f"\nName: {self.Name}\nSection: {self.Section}\nStudent ID: {self.StudentID}\nCollege: {self.collegeName}\nNo. of students: {self.NoOfStudents}")
student101=studentAKG("Aaryan Kumar", "S-1", 2410007)
student101.details()
student102=studentAKG("Ajay Kumar", "S-1", 2410123)
student102.changecollegeName("Baby Engineering College")
student102.details()
student103=studentAKG("Naresh Kumar", "S-1", 2410190)
student103.details()
student104=studentAKG("Aditya Singh", "S-1", 2410001)
student104.details()

# Illustration 2: With class method
class studentAKG:
    collegeName="AKGEC"
    NoOfStudents=0
    def __init__(self, name, sec, stdID):
        self.Name=name
        self.Section=sec
        self.StudentID=stdID
        studentAKG.NoOfStudents += 1
    # Class Method creation ~ It will change college name for all objects [NOTE]
    # Just add @classmethod decorator to the method
    '''Yha pe isko phla argument as a class milta h naki object...that's why it changes whole class variable only'''
    @classmethod
    def changecollegeName(MeriMarzi, new_college):
        MeriMarzi.collegeName=new_college
    def details(self):
        print(f"\nName: {self.Name}\nSection: {self.Section}\nStudent ID: {self.StudentID}\nCollege: {self.collegeName}\nNo. of students: {self.NoOfStudents}")
student101=studentAKG("Aaryan Kumar", "S-1", 2410007)
student101.details()
student102=studentAKG("Ajay Kumar", "S-1", 2410123)
student102.changecollegeName("Baby Engineering College")
student102.details()
student103=studentAKG("Naresh Kumar", "S-1", 2410190)
student103.details()
student104=studentAKG("Aditya Singh", "S-1", 2410001)
student104.details()


# NOTE: split() function splits the string and returns list of elements that get splitted.

# Class Method as alternative constructor
class Employee:
    def __init__(self, name, salary):
        self.Name=name
        self.Salary=salary
    # Created Class method as alternate constructor
    @classmethod
    def forString(CLASS, str):
        return CLASS(str.split("_")[0], int(str.split("_")[1]))
    
    def info(self):
        print(f"\nEmployee name: {self.Name}\nEmployee Salary: {self.Salary}\n")

emp1=Employee("Aaryan", 120000)
emp1.info()
string="Ajay_13000"
'''We made a string and passed it to and passed it to class by using class method inside class to separate it and give the original constructor of class the required arguments. '''
emp2=Employee.forString(string)
emp2.info()


# End of DAY-7
print("\n\n")
print("THIS IS END OF","#PythonPractice","#Day7",sep="~~")