def welcome():
    print("I am code5trial1.py...I am from AARYAN")

'''
__name__ will give __main__ if it directly this file is runned by user.
If user is running this from some other file then it __name__ will give name of this file
'''
print(__name__)

if __name__=="__main__":
    welcome()