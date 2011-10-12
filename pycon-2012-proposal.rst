==========================================================
Scaling Django To a Global Audience With Mozilla's Playdoh
==========================================================

Abstract
========

`Mozilla`_'s `Playdoh`_ project is a Django kit that lets you build web apps
with enhanced security, performance, localization, and ease of use. Mozilla
builds open source Django sites that typically serve millions of users from
all corners of the world. As each website evolves, any useful middleware /
module is extracted and documented to encourage re-use. Playdoh is the
culmination of this effort and Mozilla now starts all new Django projects with
Playdoh. This talk will introduce Playdoh's features, show you how to
integrate it into your own Django stack and encourage you to get involved with
the project.

.. _`Playdoh`: http://playdoh.readthedocs.org/
.. _`Mozilla`: http://www.mozilla.org/

Outline
=======

- The Man-Month Reality

  - Standard tools mean less ramp-up for contributors
  - open source
  - Django is ubiquitous

- Mozilla's Django apps

  - https://addons.mozilla.org
  - http://support.mozilla.org
  - https://input.mozilla.org
  - etc.

- Using Playdoh

  - ``git clone ...``
  - ``pip install -r requirements/compiled.txt``
  - ``./manage.py runserver``

- Security

  - http://bit.ly/django-sha2
  - http://bit.ly/django-bleach
  - monkey patches :(

- Performance

  - optional Jinja w/ template loader
  - http://bit.ly/cache-machine
  - http://bit.ly/jingo-minify
  - background tasks with celery
  - http://bit.ly/django-multidb-router

- Localization

  - Jinja / jingo helpers
  - Mozilla specific tools (ELMO? https://wiki.mozilla.org/L10n:Dashboard/Elmo)

- Ease of Use

  - http://bit.ly/django-nose
  - test speedups
  - pip
  - DB migrations
  - Sphinx docs
  - http://bit.ly/django-cronjobs
  - mobile apps

- Upstream to Django?

  - open source is hard
  - pushing to github is easy
  - Mozilla's problems != your problems

- Caveats

  - Jinja2 templates
  - Python 2.6 only
  - MySQL only (maybe)
  - vendor library as git submodule
  - L10n complexity

- Future

  - Postgres
  - better support for Django templates
  - South for migrations
  - remove Mozilla branding libs like global headers / product details?
  - vendor mgmt. tool (or pip support?)

- Get Involved

  - (your patch here)
  - report bugs, feature requests
  - MoPy mailing list?
