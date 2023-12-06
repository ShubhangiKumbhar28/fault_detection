Step 1 - Install the requirements
'''
pip install -r requirements.txt
'''

Step 2 - Run main.py file
'''
python main.py
'''

Git commands

If you want to use git in project

'''
git init
'''

Note: This is going to initalize git in source code.

OR

You can clone exiting github repo
'''
git clone <github_url>
'''
Note: Clone/ Downlaod github repo in system

Add changes made in file to git stagging are

'''
git add file_name
'''
Note: You can given file_name to add specific file or use "." to add everything to staging area

Create commits
'''
git commit -m "message"
'''

'''
git push origin main
'''
Note: origin--> contains url to github repo main--> is branch name

To push changes forcefully.
'''
git push origin main -f
'''

To pull changes from github repo
'''
git pull origin main
'''
Note: origin--> contains url to github repo main--> is branch name

.env file has