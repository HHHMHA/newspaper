#Newspaper Website
###Simple Django practice project

#1. Requirements
All the requirements are listed in [requirements.txt](requirements.txt)

however you can just activate the virtual environment with pipenv shell.

#2. Running the server
First apply the migrations:
`python manage.py migrate`

Then you're good to go
`python manage.py runserver`

#3. About the project
The core functionality is about creating, editing, and deleting articles
Basic User Authentication and Authorization is included
AJAX is used to like/dislike articles
Comment for each article

**NOTE**
Most of this project was taken form the book [Django For Beginners](https://www.amazon.com/Django-Beginners-Build-websites-Python-ebook/dp/B079ZZLRRL) so thanks to the author.