# Python 3 support
try:
    import urlparse
    from urllib import urlencode
except:
    import urllib.parse as urlparse
    from urllib.parse import urlencode

from django.conf import settings

from .const import TYPE_PARAM_NAME


def get_type_parameter_name():
    """ Get the parameter name used for type_id in pixel request. """
    try:
        type_parameter_name = settings.PIXELS_TYPE_PARAMETER_NAME
    except AttributeError:
        type_parameter_name = TYPE_PARAM_NAME

    return type_parameter_name


def compose_pixel_url(tracking_url, type_id):
    """ Insert tracking call type_id into a given pixel tracking call. """
    type_id = int(type_id)
    type_parameter_name = get_type_parameter_name()

    url_parts = list(urlparse.urlparse(tracking_url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update({type_parameter_name: type_id})
    url_parts[4] = urlencode(query)

    return urlparse.urlunparse(url_parts)
