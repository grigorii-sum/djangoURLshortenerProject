# djangoURLshortenerProject

Project "djangoURLshortenerProject" is needed for:
1. Creating short URL for inputted long URL:

`http://127.0.0.1:8000/create`

    INPUT: URL of your website
    
    OUTPUT: Short URL for redirecting to your website

2. Redirecting from short URL to long URL:

`http://127.0.0.1:8000/s/<str:short_url>`

    INPUT: URL with your short URL part
    
    OUTPUT: Page of your website

---

## STARTING PROJECT

Enter all the following commands in sequence:

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python3 manage.py migrate`

`python3 manage.py runserver`

The project is working!

---

## RUNNING TESTS

Enter the command below:

`python3 manage.py test --verbosity 1`

The tests are running!
