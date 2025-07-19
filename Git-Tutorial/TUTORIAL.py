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

git add .
Response ~ No Response
This adds everything (folders and files) to the staging area.

CHECK STATUS
git status
Response ~ 
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

        

'''