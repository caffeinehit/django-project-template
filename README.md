django-project-template
=======================

Django project template pulling settings from the environment.
Requires [`dj-database-url`](http://pypi.python.org/pypi/dj-database-url/0.2.1).

Examples:

    DEBUG=True python manage.py runserver
    DEBUG=False python manage.py runserver
    DEBUG=False DATABASE_URL=postgres://user:password@host:port/database python manage.py runserver
    DEBUG=True STATIC_ROOT=/var/www python manage.py runserver
