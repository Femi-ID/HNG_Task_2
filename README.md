# **About the HNG Task 2 CRUD Application**

This project is an application that can perform basic CRUD operations

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/).

### Set Up:
* You should have your virtual environment running in your terminal.
* You'll need to install django: django and it's rest framework
```bash 
pip install django
pip install djangorestframework
```
* The database used is SQLite, but you can use any database of your choice.
* To run the app: 
```bash 
python manage.py runserver
```
* To migrate your database: 
```bash 
python manage.py makemigrations 
python manage.py migrate
```
* To create an admin user: `python manage.py createsuperuser` and answer the prompt commands.
* Populate your database from this end or the API endpoints.
* That's basically it.


### Endpoints
The API has **3** endpoints which you can check out in the views.py:
1. **/:** The home view for all user profiles.
2. **/api:** The create user view profile
3. **/api/<user_id>:** The view for user profile detail.

**Check the [documentation](https://github.com/Femi-ID/HNG_task_2/blob/master/DOCUMENTATION.md) for more information.**
