# TOPICS COVERED
'''
1. Some Shortcuts
2. Type Casting
3. Detailing of all about 'Strings'
4. If, ELif, ELse Statements
5. Conditional operators
6. Match case Statements
'''





print("Hey!....This is my second Day")
print("Hey!....This is my second Day")
print("Hey!....This is my second Day")
# This is done using (Alt+Shift+Down)
# Also for multiple cursor in different lines (Alt + Select those lines using mouse)


# TYPE CASTING IN PYHTON
'''
Use functions:
int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict() ~ Explicit Type Casting
'''
num1=input("Enter number 1: ")
num2=input("Enter number 2: ")
print("Concatenation of number is: ", num1+num2)
# input() function BY DEFAULT takes string as an input so it gets CONCATENATED...!

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
print("Addition of number is: ", num1+num2)
# Now due to Explicit conversion int() number gets ADDED...!


# Multiline strings storing using '''.....'''
introduction='''Hi...! I am "Aaryan Kumar"
I am learning Beginner Python with CodeWithHarry
I am doing B.tech @ AKGEC
Currently BUSY...see you LATER!!'''
print("Self-Introduction:\n",introduction)
i=int(input("letter index:"))
print ("Letter at the given index is: ",introduction[i])  # string is like an array of CHARACTERS


# For printing characters in string
for character in introduction:
    print(character)


# String Slicing and length of string
string="AaryanKumar"
print(string[0:6]) # Here (0 index) will be printed but (6 index) will not be printed
print(string[:]) # Full names gets printed
print(string[:6]) # Starts automatically from 0
print(string[0:]) # automatically goes till last
print(string[0:-6]) # prints from 0 to 6th letter from back of string; 6th letter from back dont get printed
print(len(string))
# Strings are immutable
print(string.upper()) # It returns new string; previous string is immutable that is not changed
print(string.lower()) # for lower casing all letters
'''
rstrip(), replace(), count(), endswith(), startswith(), swapcase(), Find(), title():
are used also used with string in respective manner

isalnum(), isalpha(), islower(), isupper(), isprintable(), isspace(), istitle():
checks whether string is in required format

split() ~ convert into list, items in string should be separated by spaces
capitalize() ~ capitalizes first letter of string and lowercase all other layers
center() ~ to the enter in console
count() ~ 
'''



# Using if, elif, else 
'''
FORMAT:
if(condition):
    ....
elif(condition):
    ....
else:
    ....
'''

# CONDITIONAL OPERATORS
# <, >, <=, >=, ==, !=


# MATCH CASE STATEMENTS ~ WORKS ONLY ON PYTHON 3.10 ~ Analogy with SWITCH in C programming

input=int(input("number="))  # Taking input to match 
#FORMAT
# NOTE- No break statement is used here like in C
match input: # "switch" is replaced by "match" in python 
    case 1:
        print("this is case 1")
    case 2:
        print("This is case 2")
    case 3:
        print("This is case 3")
    case 4:
        print("This is case 4")
    case 5:
        print("This is case 5")
    case 6:
        print("This is case 6")
    case 7:
        print("This is case 7")
    case _ if input<10: # "default" is replaced by "_" in python
        print("This the DEFAULT case, the given input is less than 10")
    case _ if input<20:
        print("This the DEFAULT case, the given input is less than 20")
    case _ if input<50:
        print("This the DEFAULT case, the given input is less than 50")
print("\n\n")
print("THIS IS END OF","#PythonPractice","#Day2",sep="~~")