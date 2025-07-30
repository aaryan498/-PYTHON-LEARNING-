# Topics Covered:
'''
1. Time module in Python
2. Use of Walrus Operator (:=)
3. Shutil module ~ built-in module
4. Requests module in Python ~ External module
5. Generators in Python
6. Funtion Caching in Python
'''





# Time module in Python

# Illustration 1: To calculate the time taken by program to run ~ using time.time()

import time
'''
time.time() is funtion of time module that return the time in seconds that passed since 1970 till current time.
'''

def forLoop():
    for i in range(5):
        print(i)

def whileLoop():
    i=0
    while (i<5):
        print(i)
        i += 1

init1=time.time()
forLoop()
t1=time.time()-init1

init2=time.time()
whileLoop()
t2=time.time()-init2

print("Time taken by for loop: ",t1,"seconds")
print("Time taken by while loop: ",t2,"seconds")
print(time.time())


# Illustration 2: using time.sleep()
'''
pass the seconds for which you want to stop the code, inside time.sleep(seconds) and program will freeze for that many seconds.
'''

forLoop()
time.sleep(1)
whileLoop()

# Illustration 3: using localtime() and strftime()
'''
time.strftime() ~ is used to get the time in required format.
'''
print(time.localtime())             # see the output of how it works
date=time.strftime('%d.%m.%Y')
time=time.strftime('%H:%M:%S')
print("Date: ",date)
print("Time: ",time)



# Use of Walrus Operator (:=)
'''
Using this operator we can assign a value to a variable within an expression.
'''
# Illustration 1: Simple example
a=True
print(a:=False)

# Illustration 2: A program without walrus operator
foods=[]
food=''
while(food!='quit'):
    food=input("What food do you like: ")
    if food!='quit':
        foods.append(food)
print(foods)

# Illustration 3: With walrus operator
foods=[]
while(food := input("Enter your favorite food: ")) != 'quit':
    foods.append(food)
print(foods)




# Shutil module ~ built-in module 
'''
1. This is a powerful module...often use to copy a tons of files from different folders and paste it to required destinations.
2. It can use for many function like copying files and folders, moving files from 'src' to 'dest.'
'''
import shutil
shutil.copy("file.txt","copy_file.txt")
'''
NOTE:copy the whole content of file from source file 'file.txt' and creates a destination file and paste all content there. It does copy and paste the meta data.
'''

shutil.copy2('file.txt','copy_file2.txt')
'''
It is updated version of shutil.copy2()...
It copies the meta data of source file and paste it in destination file.
NOTE: Meta data is the type of data like date of creation and time of creation it's language type and so on.
'''

# shutil.copytree("folder","copied_folder")
'''
1. It is used to copy full Folder and all files inside it and paste it to destination folder.
2. Uncomment it when you want to use it.
NOTE: The shutil.copy() and shutil.copy2() only copies the files and not the folder.
'''

# Automatic creation of files
import os
import time
for i in range(15):
    shutil.copy2("file.txt", f"file-{i+1}.txt")



# Automatic cleaning of files in interval of 5 seconds
time.sleep(5)
for i in range(15):
    os.remove(f'file-{i+1}.txt')

time.sleep(5)
os.remove("copy_file.txt")
os.remove("copy_file2.txt")



# Requests module in Python ~ External module
'''
1. It is often useful in case you want to 'get' or 'post' requests on any URLs.
2. It is often use for scraping in html pages like for example getting all <h2> headings from any HTML code of webpage.
3. Installation ~ 'pip install requests' ~ type this in Cmd prompt
4. For more info on this topic, go to Video-#89
'''



# Generators in Python 
'''
It acts like a list but it does not store the values....rather generates the value on the fly while working.
'''
def generator():
    for i in range(11):
        yield i*2


gen=generator()
for i in gen:
    print(i)

# To print only one value use this method
gen1=generator()
print(next(gen1))



# Funtion Caching in Python
'''
1. It is used in case of Expensive function which takes more time to execute due to complex computations.
2. To use this Import 'functools' and use decorator '@functools.lru_cache(maxsize=your wish) above the function for which you want to store cache.
3. This should be used only for small number of values, and do it only if you value passing to the function might get repeated, Otherwise it will waste memory.
4. Also remember, that when you restart the program the cache memory gets cleared and it will again stor the cache accordingly.
'''

from functools import lru_cache
from time import sleep

@lru_cache(maxsize=None)
def sleepy_function(n):
    sleep(3)
    print(f"I am done for {n}")
    return n*1000

# Running for first time ~ each one will take 3 seconds to execute
print(sleepy_function(1))
print(sleepy_function(2))
print(sleepy_function(3))
print(sleepy_function(4))


'''Running same thing for second time ~ goes instantly because it doesn't undergo computation...It's result is already stored in cache memory so the result get displayed instantly without sleeping for 3 seconds.'''
print("I am done for 1\n",sleepy_function(1))
print("I am done for 2\n",sleepy_function(2))
print("I am done for 3\n",sleepy_function(3))
print("I am done for 4\n",sleepy_function(4))

# Again running for a new value ~ now this will again sleep for 3 seconds because it's value is not known by cache.
print(sleepy_function(99))
