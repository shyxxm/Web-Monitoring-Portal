Web Monitoring Portal : https://youtu.be/yz4YCvPHKds

1) Setup

The first thing to do is to clone the repository:
$ git https://github.com/shyxxm/Web-Monitoring-Portal.git


2) Create a virtual environment to install dependencies in and activate it:

py -m venv env #creates virtual environment
.\env\Scripts\activate #file path for activating virtualenv

3) Then install the dependencies:

pip install -r requirements.txt  { #if you are using someone's django code, most likely they will have a requirements.txt file which includes all their external packages and libraries }

4) Using the database:

Install postgressql:
https://www.postgresql.org/download/

- Create and setup your account
python manage.py makemigrations #importing migrations
python manage.py sqlmigrate monitor 0001
python manage.py migrate

Project Description:

https://youtu.be/yz4YCvPHKds

Frontend:
1) HTML
2) CSS
3) Javascript

Backend:
1) Python
2) Django Web framework
3) PostgreSQL
