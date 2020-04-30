 [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
  <a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif" border="0" alt="A Django project." title="A Django project." /></a>
 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<h1>Suspect Management System</h1>
<p>This is a project where a witness can identify the suspect without actually revealing his identity.</p>

<p>This makes use of Python3, Django and react(still implementing).</p>

<h1> Commands to run the code: </h1>
<p>Come to the suspect directory.</p>
<p>Activate a virtual environment and then type the following commands</p>
```
$ python -m pip install Django
$ pip install django-crispy-forms
$ pip install django-phonenumber-field[phonenumberslite]

```
<p> You could be asked to install Pillow </p>
```
$ python -m pip install Pillow
```
<p> Now you can run the server: </p>
```
$ python manage.py migrate
$ python manage.py runserver
```
<p> Now head over to http://127.0.0.1:8000/ to view the website.</p>
<p> After logging in you can visit http://127.0.0.1:8000/posts to look at the suspects and identify the criminal.</p>
<p> You can go to http://127.0.0.1:8000/admin to go to the admin page. </p>
