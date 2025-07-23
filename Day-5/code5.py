# TOPICS COVERED:
'''
1. Short Hand If-Else statements
2. Enumerate Function in Python
3. HOW TO INSTALL AND USE VIRTUAL ENVIRONMENT IN PYTHON AND IMPORTING MODULES
4. OS module in python
5. Local and Global Variables in Python
6. FILE HANDLING IN PYTHON ~ VERY VERY VERY IMPORTANT
7. Using readline() and writeline() in Python

NOTE: To see the result of various Illustrations in File Handling 'comment out' other Illustrations to remove their effects.
Use Manual checking in case of File handling
'''







# Short Hand If-Else statements

# Illustration 1:
a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
print("a is greater than b") if (a>b) else print("a is equal to b") if (a==b) else print("b is greater than a")
c= 9 if (a>b) else 0
print(c)

# Enumerate Function in Python

# Illustration 1: Without Enumeration
marks=[12,45,98,56,32,44,21,33]
index=0
for mark in marks:
    print(mark)
    if(index==2):
        print('Aaryan')
    index+=1

# Illustration 2: With Enumeration
'''
It gives its index and its value at the same time
It unpacks the Tuple actually 
format should always be index, value
If instead of index, value you write only one variable you will get a tuple
'''
marks=[12,45,98,56,32,44,21,33]
# Illustration 1:
for mark in enumerate(marks):
    print(mark)
    if(index==2):
        print('Aaryan')
# Illustration 2:
for index,mark in enumerate(marks):
    print(mark)
    if(index==2):
        print('Aaryan')
    




# HOW TO INSTALL AND USE VIRTUAL ENVIRONMENT IN PYTHON
'''
1. See video Day-#43
2. If you want to use different versions of python in single computer then you can use virtual environment
'''



# Impoting Modules
'''
use code like: 
1. import math                    # Simply to import math
2. from maths import sqrt(),pi    # To import particular functions from math
3. import math as m                  # Now you can Access math using m.sqrt()
To print functions present in any module we use dir function like:
'''
import math as m
print(dir(m))
'''
NOTE: INTRESTING USE:
If you make any function in any other file and import it using:
from file_name import function,variables_of that file
you can use it here in this file also 
NOTE: file should be in same folder
'''
from code5trial import trial_function
trial_function()


'''
The code below will execute welcome() function twice.
To avoid this we use [if __name__=="__main__"] in source file which is imported.
'''
import code5trial1
code5trial1.welcome()




# OS module in python 
'''
1. Refer to video Day-#46
2. This file consists of large amount of functions that can used to automate many things in python.
3. Functions like forming a file inside 1000 of folders...controlling naming and renaming and checking entries inside different folders.
4. This topic needs to explored on your own basically. 
os.cwd(), osmkdir(), os.path.exists(), os.rename(), os.listdir(), os.system(), os.chdir()
'''



# Local and Global Variables in Python 

# Illustration 1: Global variable remains unchanged here
x=6
print(x)
def funct():
    x=5
    print(f"The LOCAL value of x is {x}")
print(f"The global value of x before calling function is {x}")
funct()
print(f"The global value of x after calling function is {x}")


# Illustration 2: How to change Global variables using Functions
x=6
print(x)
def funct():
    global x
    x=5
    print(f"The LOCAL value of x is {x}")
print(f"The global value of x before calling function is {x}")
funct()
print(f"The global value of x after calling function is {x}")





# FILE HANDLING IN PYTHON ~ VERY VERY VERY IMPORTANT

# Illustration 1: Reading in File Handling
f=open("myfile.txt","r")
# print(f)
text_data=f.read()
print(text_data)
f.close()

'''
SOME FACTS
1. 'r' is reading mode and it throws error if file don't exists.
2. 'w' is write mode, it opens new file if it does not exists.
3. Writing anything in file in write mode deletes it's previous content.
4. 'a' is append mode
5. 'a' does not delete previous content it adds extra content to it
6. 'r' mode is default in opening the file, if don't give any mode it take it as 'r'.
7. 'x' is create mode and ir creates required file and throws error if file already exists.
8.'rt' it opens a text file in readable mode
9. 'rb' opens in binary form.
10. binary form is used read images in png, jpg, etc.
'''

# Illustration 2: Writing in File
f1=open('myfile2.txt','w')
f1.write("Hey I am first text in second file")
f1.close()
f1=open('myfile2.txt','r')           
text=f1.read()
print(text)
f1.close()
f1=open('myfile2.txt','w')
f1.write("Heyaaa!!!...I am the second file with second text")
f1.close()
f1=open('myfile2.txt','r')           
text=f1.read()
print(text)
f1.close()

# Illustration 3: Appending in File Handling in python

f1=open('myfile2.txt','a')
f1.write("Hey I am first text in second file")
f1.close()
f1=open('myfile2.txt','r')           
text=f1.read()
print(text)
f1.close()
f1=open('myfile2.txt','a')
f1.write("Heyaaa!!!...I am the second file with second text")
f1.close()
f1=open('myfile2.txt','r')           
text=f1.read()
print(text)
f1.close()

# Illustration 4: Usage of 'with' in File handling ~ To avoid closing it...'with' automatically closes it after operation.

with open('myfile2.txt','w') as f1:
    f1.write("REWRITING while using 'with'")
with open('myfile2.txt','r') as f1:
    text=f1.read()
    print(text)

# Illustration 5: TO read a file line by line ~ readline()
f=open('myfile.txt','r')
while True:
    line=f.readline()
    if not line:
        print("No line left...bye!")
        break
    print(line)   
f.close() 

# Illustration 6: Writing line by line in file ~ writeline() ~ [clarify using chatGPT]
f=open('myfile2.txt','w')
lines=['1. This is my first line\n','2. This is my second line\n','3. This is my third line\n']
f.writelines(lines)
f.close()
f=open('myfile2.txt','r')
lines=f.readlines()
print(lines)

# End of DAY-5
print("\n\n")
print("THIS IS END OF","#PythonPractice","#Day5",sep="~~")
