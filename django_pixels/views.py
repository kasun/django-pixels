from django.http import HttpResponse

from .utils import get_type_parameter_name
from .exceptions import PixelError
from . import handlers


def pixel(request):
    type_parameter = get_type_parameter_name()
    type_id = request.GET.get(type_parameter)
    if not type_id:
        return HttpResponse(204)

    try:
        handler = handlers.get_handler(type_id)
    except PixelError:
        pass
    else:
        handler(request)

    return HttpResponse(204)
