=====
Polls app for jenkins CI
=====

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Include the polls URLconf in your project urls.py like this:

    url(r'^polls/', include('polls.urls')),

3. Run `python manage.py migrate` to create the polls models and model scheme.
4. Add a superuser by running the command `python manage.py createsuperuser' and enter username and password.
5. Add username and password . Now you can login with the same credentials in your admin page.
6. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

7. Visit http://127.0.0.1:8000/polls/ to participate in the poll.

PYPI Distribution
-----------------

Can be found at https://pypi.python.org/pypi?name=django-polls_1_10&version=0.1&:action=display
