Project Title
Build on django Rest Api

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Prerequisites
What things you need to install the software and how to install them

Give examples
Installing
A step by step series of examples that tell you how to get a development env running

Before we install Django, create a virtual environment (also called a virtualenv)

python -m venv myvenv
The command above will create a directory called myvenv (or whatever name you chose) that contains our virtual environment (basically a bunch of directory and files). 
Start your virtual environment by running:

C:\Windows\System32\ToDo1> myvenv\Scripts\activate
Now that you have your virtualenv started, you can install Django. 
Before we do that, we should make sure we have the latest version of pip, the software that we use to install Django:

(myvenv) ~$ python -m pip install --upgrade pip
Installing packages with requirements
A requirements file keeps a list of dependencies to be installed using pip install:

First create a requirements.txt file inside of the ToDo1/ folder. You do this by opening a new file in the code editor and then saving it as requirements.txt in the ToDo1/ folder. 
In your ToDo1/requirements.txt file you should add the following text: 
Django~=2.0.6 
Now, run pip install -r requirements.txt to install Django.

command-line

(myvenv) ~$ pip install -r requirements.txt
Running the tests
I have run 10 tests for this project. All test is inside of tests folder in webapp. Inside this there are two files test_models, test_views.

C:\Users\esatnir\Videos\ToDo1\webapp\tests
test_models contains test of model.py and test_views contains test of views.py 
to run these tests, run the following command.

(myvenv) C:\Users\esatnir\Videos\ToDo1>python manage.py test
Deployment
On Windows you should run the following command.

(myvenv) C:\Windows\System32\ToDo1> python manage.py runserver
Built With
Python 3.7.1 - Programming Language
Django 2.0.0 - The Web Framework
Database - SQLite
