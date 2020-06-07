Little Demo of Python & Django with Celery Task Management (https://docs.celeryproject.org/en/stable/index.html)

To install: Create virtual environment (https://www.geeksforgeeks.org/python-virtual-environment/) --> "pip install -r requirements.txt"

To run server "python manage.py runserver" & to run celery server "celery -A taskmanagement worker -l info".

A message Broker e.g. Redis is needed & to be configured in settings.py.

At the moment everything that happens is that the localhost website is displayed directly and the sleeping task is running in the background.
(This can be seen in Celery Terminal)