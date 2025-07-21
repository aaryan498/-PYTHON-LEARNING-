# USE OF FOR LOOPS (DIFFERENT FROM C)

# Example 1:
name="Aaryan"
for letter in name:
    print(letter,end=("~"))

# Example 2:
colours=["red","green","blue","yellow"]
print("\n")
for colour in colours:
    print(colour)
    for letter in colour:
        print(letter)

# Example 3:
for k in range(1,8):  # 1 will be INCLUDED while 8 will be EXCLUDED
    print(k)

'''
NOTE: 
range() function has three arguments in total 
FORMAT of range():
range(start,stop,step)
1. you can choose to give only Stop argument, python will by default take start as 0 and step as 1
2. step is the difference between two values of looping variable(k)
'''

# Use of While loop
'''
It is used in simailar manner as in C programming.
NOTE: we can use ELSE with while loop here, whe the first time while loop condition gets false the else block gets executed
'''
# Example 1:
i=1
while(i<5):
    print(i)
    i=i+1
else:
    print("I am in else block")


# NOTE: 'Do WHile' is not there in python


# BREAK AND CONTINUE is usesd as used in C programming


# FUNCTIONS IN PYTHON

# Illustration 1:
def AreaOfCircle(r):
    '''
    1. Here in this function r is required argument
    2. can make a funtion like def Area(r=4)  ~ this is the default argument
    Also, learn in deep about default, keyword, required, Variable length arguments.
    '''
    area=3.14*r*r
    print(area)
a=4
AreaOfCircle(a)

# Illustration 2: (Using Variable Length Argument)-tuple example
def average(*numbers):
    print(type(numbers))  # it takes numbers as tuple in argument, so we an take n number of arguments.
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average of numbers is:",sum/len(numbers))

average(2,3,5,6,45,34)

# Illustration 3: Dictionary argument example
def wisher(**name):
    print("Hello",name["fname"],name["mname"],name["lname"])

wisher(fname='Aaryan',mname='',lname='Kumar')

# Illustration 4: return value from function
def CircleArea(r):
    formula=3.14*r*r
    return formula
    return 7  # nhi mana jayega phla return will be taken into consideration, so no effect
a=4
area=CircleArea(a)
print(area)



# Lists in Python ~~ Operations in Lists
'''
1. mutable ~ can be changed, that means values can added, removed or changed in same list
2. denoted by square brackets
'''
marks=[2,4,5,"Aaryan",True, False, 9,7,81]
print(type(marks))  # To detect the datatype
print(marks)        # To print the list
marks.append("Singham") # Adding items to list
print(marks)        # TO show that same list can be mutated
marks[5]="Kumar"    # To change element of list
print(marks)
print(marks[2])     # To print element of list
print(marks[1:8:2]) # 1:8 is used for slicing and lest one is used for jumping       
#NOTE: SLICING IN LIST IS DONE SAME AS DONE IN STRINGS, Also take NEGATIVE SLICING in consideration, which is same as string
print(marks[:-3])   # same as print(marks[:len(marks)-3])

# Illustration 1: use of 'in' ~ HAPPENS IN CASE OF 'STRINGS' AND 'TUPLES' ALSO
if "Aaryan" in marks:
    print("Aaryan is there in list")
else:
    print("Aaryan is NOT in list")
if "ary" in "Aaryan":     # Same happens in case of STRINGS also
    print ("yes")

# LIST COMPREHENSION ~ basically to describe what is inside list
# Illustration 1:
list1=[i for i in range(45) if i%2==0]   # contains even numbers from 0 to 45
list2=[i*i for i in range(10) if i%2==0]
print(list1)
print(list2)

# Operations on list
# NOTE: To see the Effect of each operation comment out other lines
list3=[65,3,2,9,34,54,9,89,9,65,12,16,19]
list3.append(26)               # ADD the item to end of list
list3.sort()                   # Arrange items in Ascending Order
list3.sort(reverse=True)       # Arrange items in Descending Order
list3.reverse()                # Reverses the original string
list3.count(9)                 # counts the number of occurences of particular item in list
# print(list3.index(9:4:9))      # Returns index value of item, first argument is item ...while next two is used for slicing the list to search item ~ DOUBT (RETURNS ERROR)
copy_list=list3.copy()         # Always use this in case you want to copy a list to another variable
# copy=list3                   # Never use this because changes in 'copy' will reflect in 'list3' also
list3.insert(2,992)            # Inserts 992 at index 2 of list3
print(list3)
list4=[221,451,891] 
list3.extend(list4)
print(list3)
concatenate=list3+list4        # To concatenate two list



# Tuples
# Cannot be mutated ~ immutable
tup=(2,45,67,"green",False)
# tup(0)=92       # causes error ~ immutable
print(type(tup))
if 45 in tup:
    print("yes")
else:
    print('no')

# Slicing in tuple ~ NOTE: NEW TUPLE is formed in this case previous tuple remains unchanged
tup2=tup[1:4]
print(tup2)


# Operations on Tuple
'''
Operations on Tuple is not done directly...first it is converted into list then required changes are made
And then it is converted back into tuple
'''
# count(), index(), in tuple is used as used in lists
names=("Aaryan","Arpit","Ritu","Naveen")
print(names)
temp=list(names)
temp.append("Gaurav")
temp.pop(3)
temp[0]="AARYAN"
print(temp)
names=tuple(temp)
print(names)
names2=("krishna","shankar","shambhu")
new_name=names+names2                     # Concatenation in this way is possible, it forms new tuple
print(new_name)   

# Illustration:
tup3=(1,2,3,2,3,2,1,4,5,6,7,3,4,2,4,3,4,5)
# index=tup3.index(3:7:15)  # [Doubt], it returns error, 3: item, 7:15 ~ slicing


print("\n\n")
print("THIS IS END OF","#PythonPractice","#Day3",sep="~~")






