=============================
django-pixels
=============================

Tracking pixels made easy

Features
----------
* Built-in view to serve a pixel response
* Compose pixel tracking urls with different type IDs
* Route tracking requests to functions using type IDs

Implementation Notes with Short Examples
----------

Install django-pixels::

    pip install django-pixels


Mount pixel tracking URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
        url(r'^tracker/', include('django_pixels.urls', namespace="pixels")),
        ...
    ]


Get the general pixel tracking url (This serves a transparent pixel as the response):

.. code-block:: python

    from django.core.urlresolvers import reverse
    tracking_url = reverse('pixels:pixel') # given you have mounted django_pixels urls with namespace='pixels'

Get the tracking url with no-content(204) response (This serves an empty response with code 204):

.. code-block:: python

    from django.core.urlresolvers import reverse
    tracking_url = reverse('pixels:pixel-204') # given you have mounted django_pixels urls with namespace='pixels'


Generate a pixel tracking url with type 1:

.. code-block:: python

    from django_pixels import utils

    utils.compose_pixel_url(tracking_url, 1)


Write a function to handle tracking calls with type 1:

.. code-block:: python

    def track_emails(request):
        # handle tracking with the passed HttpRequest instance


Register the function to handle tracking calls with type 1:

.. code-block:: python

    from django_pixels import handlers

    handlers.register(1, track_emails)


Or mark a function to handle tracking calls with type 2:

.. code-block:: python

    from django_pixels import handlers

    @handlers.track(type_id=2)
    def track_emails(request):
        # handle tracking with the passed HttpRequest instance


Settings
----------
* PIXELS_TYPE_PARAMETER_NAME - Change the parameter name used for tracking type


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
