Scaling Django To a Global Audience With Mozilla's Playdoh
==========================================================

Abstract
--------

Mozilla's Playdoh project is a Django kit that lets you build web apps with
enhanced security, performance, and localization. Mozilla builds Django sites
that typically serve millions of users from all corners of the world. As each
site evolves, the useful components are extracted and documented to encourage
re-use. Playdoh pre-configures Django with these and other open source
goodies.

Outline
-------

- The Man-Month Reality

    - Standard tools mean less ramp-up for contributors
    - open source
    - Django is ubiquitous

- Mozilla's Django apps

    - [addons.mozilla.org](https://addons.mozilla.org)
    - [support.mozilla.org](http://support.mozilla.org)
    - [input.mozilla.org](https://input.mozilla.org)
    - etc.

- Using Playdoh

    - `git clone ...`
    - `pip install -r requirements/compiled.txt`
    - `./manage.py runserver`

- Security

    - [django-sha2](http://bit.ly/django-sha2)
    - [django-bleach](http://bit.ly/django-bleach)
    - monkey patches :(

- Performance

    - optional Jinja w/ template loader
    - [cache-machine](http://bit.ly/cache-machine)
    - [jingo-minify](http://bit.ly/jingo-minify)
    - background tasks with celery
    - [django-multidb-router](http://bit.ly/django-multidb-router)

- Localization

    - Jinja / jingo helpers
    - Mozilla specific tools ([ELMO](https://wiki.mozilla.org/L10n:Dashboard/Elmo))

- Ease of Use

    - [django-nose](http://bit.ly/django-nose)
    - test speedups
    - pip
    - DB migrations
    - Sphinx docs
    - [django-cronjobs](http://bit.ly/django-cronjobs)
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
