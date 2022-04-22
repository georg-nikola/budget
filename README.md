# Budget

A simple personal budgeting web app.

## Try it out
https://budget-project-demo.herokuapp.com/

## Local install
###Requirements
Python 3.8 or newer
Pip 21.x.x or newer
Docker
All other requirements are listed in the requirements.txt file
###Setup
Pull the repo locally
```shell
git clone https://github.com/georg-nikola/budget.git
```
Set up a sample postgres DB with docker
```shell
cd ./budget
docker-compose up -d
```
Create virtual environments and install requirements
```shell
cd ./budget
python3 -m venv /path/to/new/virtual/environment
source /path/to/new/virtual/environment/bin/activate
pip install -r requirements.txt
```
Run the app using the built-in Django runserver
```shell
python ./manage.py runserver
```
Enjoy