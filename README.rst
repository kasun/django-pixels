=============================
django-pixels
=============================

Pixels tracking made easy

Quickstart
----------

Install django-pixels::

    pip install django_pixels

Add django-pixels's URL patterns:

.. code-block:: python

    from django_pixels import urls as django_pixels_urls


    urlpatterns = [
        ...
        url(r'^tracker/', include(django_pixels_urls), namespace="django_pixels"),
        ...
    ]

Features
--------

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
