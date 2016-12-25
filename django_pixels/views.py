from django.http import HttpResponse

from .utils import get_type_parameter_name
from .exceptions import PixelError
from . import handlers


def serve(request, response):
    type_parameter = get_type_parameter_name()
    type_id = request.GET.get(type_parameter)
    if not type_id:
        return response

    try:
        handler = handlers.get_handler(type_id)
    except PixelError:
        pass
    else:
        handler(request)

    return response


def pixel204(request):
    """ Return a 204 response. """
    response = HttpResponse(204)
    return serve(request, response)


def pixel(request):
    """ Return a transparent pixel. """
    pixel_= "\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b"
    response = HttpResponse(pixel_, content_type='image/gif')
    return serve(request, response)
