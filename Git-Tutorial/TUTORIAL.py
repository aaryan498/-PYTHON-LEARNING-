# Check whether Git is Installed in system
'''
USE COMMAND PROMPT OR VS CODE TERMINAL 
Type 'git --version' ~ To check whether Git is installed, it will show Git version if installed
'''

# TO SETUP: Further in Terminal TYPE:
'''
git config --global user.name "aaryan498"
git config --global user.email "kumaraaryan498.com"
'''

# To check if setup is complete
'''
Type:
git config --list

It will show your User name and Email
'''

# Some Command and their meanings
'''

git init → Starts Git in your current folder.

git remote add origin ... → Links your local folder to the GitHub repo.

git branch -M main → Sets your branch name to main (default on GitHub).

git push -u origin main → Uploads your local files to GitHub for the first time.
'''

# Process to do 

# STEP 1: Connecting Folder with Repository
'''
git init
Response ~ Initialized empty Git repository in C:/Users/homeuser/Desktop/#BeginningPythonPractice/.git/

git remote add origin https://github.com/aaryan498/-PYTHON-LEARNING-.git
No response ~ It will link your folder with GitHub account

Verify the connection:
git remote -v
Response:
origin  https://github.com/aaryan498/-PYTHON-LEARNING-.git (fetch)
origin  https://github.com/aaryan498/-PYTHON-LEARNING-.git (push)
'''

# STEP 2: Staging Your Files ~ Ready to Push
'''
git add .
Response ~ No Response
This adds everything (folders and files) to the staging area.

CHECK STATUS
git status

Response ~ 

Example1 ~ This happens when you change anything in the file after typing command 'git add .' in the terminal: (FAIL)

On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   #Day1-Variables&Datatypes/code1.py
        new file:   #Day2/code2.py
        new file:   #GitTutorial/TUTORIAL.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   #GitTutorial/TUTORIAL.py

Example 2: when you dont change anything after the 'git add .' command:  (SUCCESS)

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   #Day1-Variables&Datatypes/code1.py
        new file:   #Day2/code2.py
        new file:   #GitTutorial/TUTORIAL.py


        


        
git commit -m "Initial commit: Added #Day1, #Day2, #GitTutorial folders"
Here in Double Quotes is the message That is general so describe in own words about the changes

Response ~ 
[master (root-commit) d2e0b62] Initial commit: Added #Day1, #Day2, #GitTutorial
 3 files changed, 136 insertions(+)
 create mode 100644 #Day1-Variables&Datatypes/code1.py
 create mode 100644 #Day2/code2.py
 create mode 100644 #GitTutorial/TUTORIAL.py
'''

# STEP 4: Pushing the Folders and Files
'''
Since your branch is currently named master but GitHub uses main, we’ll fix that and then push:
git branch -M main


git push -u origin main
NOTE: This code is only for first time push
'''
# Files get pushed into the Repository SUCCESSFULLY....!


# For further changes in the Files ~ USE COMMAND
'''
git add .
git commit -m "Your message"
git push

AND THE CHANGES GETS PUSHED INTO THE REPOSITORY
'''
STATUS="COMPLETED SUCCESSFULLY"
print("The Git Pushing Tutorial is",STATUS,sep=" ~ ")