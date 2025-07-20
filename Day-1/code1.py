'''
Topics covered:
1. Pip and Modules
2. Comment, Escape sequence, print()
3. Variables and Datatypes
'''

'''
In command Prompt 
Type 'python' to access python
Type 'pip' to know about utility 
Type 'pip install pandas' to istall external modules(eg.~ Pandas, scikit learn, tensorflow)

Examples of Internal modules are os, math, etc.
Internal modules can be imported without been installed while, External modules needs to be installed before importing
'''


# Use command: 'cd "#Day1"' in the terminal to get in into the folder inside the main folder opened in VS code.
'''
This is used for multiline comment.
You can use double quotes instead
'''
# Use (Ctrl+`) to comment/uncomment any single line.


print("Hello World...!!")
print("Hey I am a \"Good Boy\"\nMy brother is a Good Boy") # Here \" and \n are the escape sequence characters
'''
Here \" is used for using double quotes which is to be rinted in the output
\n is new line character'''


print("I am learning to use Separate","Line got separated by separate character \"--\"",sep="--",end="--")
print("This is new line",end="\n")
print("This is also new line in NEXT line")
'''sep="" is used to separated different variables written in print statement by using sep charactacter
   end=""is used to append new print line statement'''


Name="Aaryan" #string
Age=19 #integer
AGE="19" #string
Health=59.9
ComplexNumberVariable=complex(1,2)
print("The type of Name variable 'Name','Age','AGE','Health' is", type(Name),type(Age),type(AGE),type(Health),"respectively") # used to check the DATATYPE of variable
print(ComplexNumberVariable, type(ComplexNumberVariable))

list1= [8,4.5,["apple","banana"]] # Lists ~ Mutable, Uses []
print(list1, type(list1))
tuple1= (("parrot","parrow"),(5,7.9)) # Tuple ~ Immutable, Uses ()
print(tuple1,type(tuple1))
dict1= {"name":"Aaryan","age":19,"CanVote":True} # Dictionary ~ Links one with another, use {}
print(dict1, type(dict1))
print("\n\n")
print("THIS IS END OF","#PythonPractice","#Day1",sep="~~")