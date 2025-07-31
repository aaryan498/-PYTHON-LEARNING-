# Topics Covered:
'''
1. Regular Expressions in Python
2. Async IO in python
3. Multi-threading in Python
4. Using concurrent.futures module in python
5. Multiprocessing in Python
'''



# Regular Expressions in Python
'''
Regular expressions (regex) in Python let you search, match, or manipulate text patterns using the re module — useful for tasks like validating emails, extracting numbers, or replacing words.

Use python documentation for complete guide on regular documentation.
For Meta characters in 're' module refer to IBM documentation.
'''
# This is an built in module.
import re



# Async IO in python
'''
1. It is a built-in module in Python.
2. The asyncio module lets you write asynchronous code that runs tasks concurrently using async/await, ideal for I/O-bound operations like APIs or file handling.
'''
import asyncio
import requests
import os
import time

async def imagedownloader1():
    URL="https://images.pexels.com/photos/3861959/pexels-photo-3861959.jpeg"
    response=requests.get(URL)
    open("EndOfBeginnerPython1.jpg","wb").write(response.content)
    await asyncio.sleep(2)
    print("Function 1 work is done.")
    return "Function 1"

async def imagedownloader2():
    URL="https://images.pexels.com/photos/1102797/pexels-photo-1102797.png"
    response=requests.get(URL)
    open("EndOfBeginnerPython2.jpg","wb").write(response.content)
    await asyncio.sleep(2)
    print("Function 2 work is done.")
    return "Function 2"

async def imagedownloader3():
    URL="https://images.pexels.com/photos/8989458/pexels-photo-8989458.jpeg"
    response=requests.get(URL)
    open("EndOfBeginnerPython3.jpg","wb").write(response.content)
    await asyncio.sleep(2)
    print("Function 3 work is done.")
    return "Function 3"

async def one_by_one_executer():
    await imagedownloader1()
    await imagedownloader2()
    await imagedownloader3()
    return "Done One-by-One"

async def asynchronous_executer():
    L=await asyncio.gather(imagedownloader1(),imagedownloader2(),imagedownloader3())
    print(L)

asyncio.run(asynchronous_executer())
asyncio.run(one_by_one_executer())

command=input("Do you want to delete the downloaded image files; Enter [yes/no]:")
if command=="yes":
    print("Removing files that are downloaded...!")
    time.sleep(2)
    os.remove("EndOfBeginnerPython1.jpg")
    os.remove("EndOfBeginnerPython2.jpg")
    os.remove("EndOfBeginnerPython3.jpg")
    print("Done...!")




# Multi-threading in Python
'''
1. We use it using buit-in module called threading.
2. The threading module enables concurrent execution of code using multiple threads, best for speeding up CPU-light, I/O-heavy tasks
'''

'''
Inko basically tb use krna chaiye when function codes takes long time to execute like for example we have to download 10 files of size 1GB each...If we do it one-by-one it will take so much time but when we use multi-threading we can start downloading all 10 files parallely and out net speed gets used completely and speed of our program increases...also further code can get executed till the files will get downloaded.
'''

import threading
import time

def func(sec):
    '''Jab ye statement print hoga mtlb funtion code ka execution start ho gya hai wha se.'''
    print(f"I am going to sleep for {sec} seconds")
    time.sleep(sec)
    print(f"I slept for {sec} seconds")
    '''jab ye statement print hoga mtlb ki ye function ka code execute ho gya hai...So observe output very carefully about when the function code execution starts and when it gets ended.'''

# Performing tasks one-by-one 
t1=time.perf_counter()
func(6)
func(4)
func(2)
t2=time.perf_counter()
print("Time taken to execute one-by-one: ",t2-t1,"\n")
# Output = 12 secs


x1=threading.Thread(target=func, args=[6])
x2=threading.Thread(target=func, args=[4])
x3=threading.Thread(target=func, args=[2])

'''Yha pr thread start krke code aagey execute hona shuru ho jata hai...It does not wait for the thread to get over. So, yha ka time taken 0.something seconds hota h...Threads apne aap khtam ho jayenge jb unko hona rhega...It will stop the speed of further codes...ye faida h inka'''
t3=time.perf_counter()
x1.start()
x2.start()
x3.start()
t4=time.perf_counter()
print("Time taken to execute using threading without using join() (parallely): ", t4-t3,"\n")
# Output: 0.some secs

#NOTE: It requires to redefine the threads to restart them back.
x1=threading.Thread(target=func, args=[6])
x2=threading.Thread(target=func, args=[4])
x3=threading.Thread(target=func, args=[2])

'''Yha join() use krne se threads ek sath chl rhe h lekin aagey ke codes, ye saare threads ke execution khatam ho jaane ke baad ho rha h, that's why output 6 seconds aa rha h kyuki first thread 6 seconds le rha h and that is the maximum time baaki threads usse phle khtam ho jaa rhe h'''
t5=time.perf_counter()
x1.start()
x2.start()
x3.start()
x1.join()
x2.join()
x3.join()
t6=time.perf_counter()
print("Time taken to execute using threading while using join() (parallely): ", t6-t5,"\n")
# Output: 6 secs



# Using concurrent.futures module in python

'''NOTE: Here, Using this module It will undergo it's processes first and the further code does not get executed until the process is completed, so it is not like threading module concept.'''


from concurrent.futures import ThreadPoolExecutor
import time


def func(sec):
    '''Jab ye statement print hoga mtlb funtion code ka execution start ho gya hai wha se.'''
    print(f"I am going to sleep for {sec} seconds")
    time.sleep(sec)
    print(f"I slept for {sec} seconds")
    '''jab ye statement print hoga mtlb ki ye function ka code execute ho gya hai...So observe output very carefully about when the function code execution starts and when it gets ended.'''

# Method 1:
def PoolingDemo():
    with ThreadPoolExecutor() as execute:
        f1=execute.submit(func, 6)
        f2=execute.submit(func, 4)
        f3=execute.submit(func, 2)
        print(f1)
        print(f2)
        print(f3)
PoolingDemo()
'''Executes automatically and independently when each task get completed.'''


# Method 2: Another easy method to do same thing.
def func1(sec):
    print(f"I am going to sleep for {sec} seconds")
    time.sleep(sec)
    return f"I slept for {sec} seconds"


list1=[6,4,2]
def PoolingDemo2():
    with ThreadPoolExecutor() as execute:
        AllResults=execute.map(func1,list1)
    for result in AllResults:
        print(result)
'''Problem with this block of code is that result gets shown only after longest duration part (here 6) completes. Actually all task are completed in it's required time only, but the problem is that the for statement is written after the list of AllResults is made completely so the Result is getting printed in after 6 seconds (longest time taking element)'''
PoolingDemo2()


'''NOTE: This gets printed at last.'''
print("I am out of code")



# Multiprocessing in Python
'''
NOTE: Complete code and explanation is in pr.py file.
'''


