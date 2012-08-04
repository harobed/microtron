=========
Microtron
=========

Install
=======

With easy_install:

::

    $ sudo pip install microtron

or by hand with git and `virtualenvwrapper <http://www.doughellmann.com/docs/virtualenvwrapper/>`_ :

::

    $ git clone git://github.com/amccollum/microtron.git
    $ cd microtron
    $ mkvirtualenv microtron
    $ pip install -e ./


Required libraries :

* lxml (http://codespeak.net/lxml/)
* isodate (http://pypi.python.org/pypi/isodate/)
    

Usage
=====

::

    $ microtron-parse --help
    Usage: microtron-parse <file> <format>

    Options:
      -h, --help  show this help message and exit
    

Questions
=========

Read the code, or go to http://github.com/amccollum/microtron/


Author
======

* Andrew McCollum <amccollum@gmail.com>


License
=======

Copyright (c) 2009 Andrew McCollum
Licensed under the MIT License (http://www.opensource.org/licenses/mit-license.php)

