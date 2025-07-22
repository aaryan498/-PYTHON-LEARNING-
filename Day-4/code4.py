# TOPICS COVERED
'''
1. Concept of f-strings
2. Docstrings and PEP_8 in Python
3. Recursion
4. Sets and it's Operations
5. Dictionary and it's Operations
6. FOR LOOP with ELSE in python
7. ERROR HANDLING IN python
'''






# Concept of f-strings:

# Old Format used before:
intro="Hey! I am {1} and I am from {0}"
name="Aaryan"
country="India"
age=19.987678
print(intro.format(country,name))

# New method-Concept of f-strings ~ used in formatting of strings
print(f"Hello! I am {name}, and I am from {country} and my age is {age:.2f}")    # Makes it convienient 
variable=f"I can use this method also to print 60 as string like {2*30}"
print(variable)

# If you want to keep f-strings as it is...then use double {{}}
print(f"Hi! My name is {{name}}, and I am from {{country}}")



# DOCSTRINGS in python--[IMPORTANT]
'''
1. It is written on the first line after declaring a function...if not written then not considered
2. It is not same as Comment...because comment is ignored by python interpreter but docstrings are not.
3. Docstrings is treated specially by Python.
4. Docstrings can be printed by print(function.__doc__)
'''
def square(n):
    '''Takes in number n and returns it's square
    '''
    sqr=n**2
    return sqr
square(5)
print(square.__doc__)

# PEP_8
'''
Type "import this" in command prompt or vs code terminal...you will see that 'THE ZEN OF PYTHON' gets printed ...
It is a beautiful poem...READ IT :-)
'''

# RECURSION 

# Illustration 1: Factorial
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

# Illustration 2: Fibonacci Series



# SETS in Python
'''
1. Its unordered...does not maintain the order
2. keeps unique elements only
3. different format from dictionary
4. Can't access elements using index because it does not maintain order.
5. It can contain strings, boolean as well like lists, tuples
'''
s={12,2,1,56,3,87,2,9,9,1}
print(s)
set1={}
print(type(set1))       # output=dict ~ empty set act as dictionary
set2=set()
print(type(set2))       # output=dict
# To access items if set ~ use for...in loop
for value in s:
    print(value)


# Operations in Sets
s3={1,3,5,2,8,5}
s4={0,4,65,3,2,9}
s5={56,65,4,3,32,31}
print(s3.union(s4))     # Just gives union of s3 and s4
print(s3.intersection(s4))
print(s3,s4)
s3.update(s4)           # value of s3 itself is updated to contain s4 elements also in itself
s4.intersection_update(s5)  # s4 gets updated with only intersection values of s4 and s5
print(s4)
print(s3)
s6=s4.symmetric_difference(s3)   # symmetric difference= (AuB)-(AnB)
s7=s4.difference(s3)
print(s6)  
print(s7)                         
'''
# the following functions is used in sets and returns boolean
isdisjoint() ~ checks if there is any intersection, if there then return false.
issuperset(), issubset() are also used in same way
'''
s7.add(2)
print(s7)       # use to add ONLY ONE value to SET
s7.remove(2)    # remove gives error if items is not present in set so discard is used
print(s7)
s7.discard(5)   # does not throw error if item not present 
print(s7)
'''
del(),clear(), pop() is also used in set operations...see their functions on own when required
'''



# Python Dictionaries
'''
1. It is used to relate key with values ...so that when you print using key ..you get it's values.
2. It is Ordered
3. From examples name1 is key and Aaryan is value
'''
dic={"name1":"Aaryan","name2":"Arpit","age1":"19","age2":"20"}
print(dic["name1"])               # Throws error if not present
print(dic.get("name1"))           # Does not Throw error if not present, return "none"
print(dic.keys())                 # To print all keys in dictionary
print(dic.values())               # To print all values
print(dic.items())                # TO print both key and value

# You can Iterate the key in dictionary using this and perform action
for key in dic:
    print(f"The value corresponding to key {key} is {dic[key]}")

# TO unpack Tuple (k,v)
for k,v in dic.items():
    print(f"The value corresponding to key {k} is {v}")

# Operations on Dictionary
ep1={132:45,451:45,678:73,981:56}
ep2={666:23,779:29,998:99}
ep1.update(ep2)                       # To update ep1 with ep2
print(ep1)
ep2.clear()                           # To clear a dictionary
del ep2                               # To delete a dictionary, used in set also
ep2={}                                # To get empty dictionary
print(ep2)
ep1.pop(132)                          # To remove any item
print(ep1)
ep1.popitem()                         # To remove last item from set
del ep1[451]                          # To delete required key from dictionary
print(ep1)




# For loop with else in python
'''
1. Structure of For loop with else is as given below
2. It executes For loop first and when the condition of for loop goes wrong the elese block is executed
'''
# Illustration 1:
for i in range(8):
    print("yes I am in loop")
else:
    print("No, I am out of loop")

# Illustration 2: What happens in case of break---IMPORTANT
'''
1. The else block will not get executed...else get executed only after complete successful execution of FOR LOOP
2. This happens in case of WHILE LOOP also
'''
for i in range(8):
    print("yes I am in loop")
    if (i==4):
        break
else:
    print("No, I am out of loop")

# illustration 3:
for i in range(5):
    print("Iteration no. {} in for loop".format(i+1))
else:
    print("Executing else block")





# ERROR HANDLING IN PYTHON 
'''
1. This is used to try a certain block of code and if it causes error then leave that block and execute the further code
2. Extremely useful when there is large amount of code
'''

# Illustration 1:
num=input("Enter you number:")
try:
    for i in range(1,11):
        print(f"{num}x{i}={int(num)*i}")
except Exception as e:
    print(e)
print("HellAAAA!!!!")

# Illustration 2:

num=input("Enter you number:")
try:
    for i in range(1,11):
        print(f"{num}x{i}={int(num)*i}")
except:
    print("Ah...! Sorry ...Invalid input")

print("HellAAAA!!!!")

# Illustration 3:
try:
    number=int(input("ENTER NUMBER:"))
    array=[6,4,2,78,35,3,3,22,3]
    print(array[number])
except ValueError:
    print("Entry is not integer")
except IndexError:
    print("Index Error")

# Illustration 3: USE OF finally ~ IMPORTANT
'''
1. It is always executed
2. It gets executed in FUNCTIONS even after the function has returned, See the code below 
3. Mostly used in FUNCTIONS
'''
def func1():
    try:
        number=int(input("ENTER NUMBER:"))
        array=[6,4,2,78,35,3,3,22,3]
        print(array[number])
        return "try is successful"
    except ValueError:
        print("Entry is not integer")
        return "I returned from Value error"
    except IndexError:
        print("Index Error")
        return "I returned from Index error"
    finally:
        print("Hey!! Chaowmein...I am always executed")
tell=func1()
print(tell)

# End of DAY-4
print("\n\n")
print("THIS IS END OF","#PythonPractice","#Day4",sep="~~")






