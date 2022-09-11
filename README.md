# URL Shortener

## Tools Used

<b>Language:</b> Python <br>
<b>Frameworks:</b> Django, Django REST Framework <br>
<b>Database:</b> SQLite <br>
<b>Library:</b> Django-Rest-Knox <br>

# Project Overview

* A RESTful API using Django REST Framework to shorten any longer url.
* This App has full-fledged standard authentication system using tokens.
* Shorten url service is available for both guest and logged in users.
* However, only logged in users can able to see the list of all the shorten and longer url list.

## API Endpoints, their request methods & functionalities
* `api/register/` a user can register from this route by simply making a post request with the following json format
```
{
    "username": "demoName",
    "email": "name@demo.com",
    "password": "demoPass@123"
}
```
* After successfully registering, user will get the below response and a token.
```
{
    "user": {
        "id": 1,
        "username": "demoName",
        "email": "name@demo.com"
    },
    "token": "12440f9d571sdavn678bbc9c4447f135hfnecf4d1404f080245f3e259709jadsfn907"
}
```
* `api/login/` a register user can login by providing credential.
```
{
    "username": "demoName",
    "password": "demoPass@123"
}
```
* `api/logout/` & `api/logoutall` a single or all the users can log out.
* `shortenurl/` this is where anybody can shorten a url with a `POST` request by giving the `longurl` value. Here's the format of request.
```
{"longurl": "https://aeon.co/ideas/the-danger-of-absolute-thinking-is-absolutely-clear"}
```
* We'll get a response of shorten url as like below.
```
{
    "longurl": "https://aeon.co/ideas/the-danger-of-absolute-thinking-is-absolutely-clear",
    "shorturl": "http://localhost:8000/goZm3*"
}
```

# Quick Video Walkthough
https://drive.google.com/file/d/1fPNpLzhFfllOdvVRt95DPJMjMqFgCnQR/view?usp=sharing

# Deployed Link
https://invento.herokuapp.com/
