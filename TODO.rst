TODO
====

To fix add to guide
-------------------

+ Add :term: tag to generate glosary (`http://sphinx-doc.org/markup/inline.html#role-guilabel`_)
+ Add tag to differentiate pdf/epub/html and show appropriate images/videos, in BH-001, for example.
+ Add Navaja Negra Slides to repo
+ Add link to on-line github code and "[source]" text to direct link to raw .py code.

New cases to add
----------------

+ good practices in command line: types, default values, numeric params, restrictions...
+ Colors in console without ncurses
+ Display information in console using ASCII tables.
+ Mathematical uses for approximate and fuzzy logic matches.
+ Good code practices using PEP 8.
+ pprint to display list and dicts
+ Celery:

    + How to run N instances of each worker in Celery
    + Celery Worker auto-scaling
    + Celery good practices. Good source: `https://denibertovic.com/posts/celery-best-practices/`_
    + Celery options: `http://docs.celeryproject.org/en/latest/configuration.html#std:setting-CELERYD_MAX_TASKS_PER_CHILD`_
    + Advanced Celery: `http://vatsalad.wordpress.com/2013/02/12/what-is-celery-task-queue-where-do-i-use-it-and-how-do-i-use-it/`_
+ Django:

    + SECRET_KEY on-the-fly generated
    + Anti-fingerprinting techniques
    + Anti-scanning techniques
    + Run something at Django starts: `http://chriskief.com/2014/02/28/django-1-7-signals-appconfig/`_
+ Converting Python to C. Compiling Python. Python2exe
+ Access to environment vars using *globals()*.
+ List class vars and methods using: *vars()* and *dir()*.
+ Accessing to private vars and methods in Python. Python hasn't private visibility: _Class__attr
+ Plugin systems:

    + Create a plugins system
    + Plugin execution order
    + Plugin dependencies