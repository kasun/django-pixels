from .exceptions import PixelError


map = {}


def track(type_id):
    """ Decorator to register a function as the handler for a tracking call type. """
    type_id = int(type_id)

    def wrapper(func):
        map[type_id] = func
        return func

    return wrapper


def register(type_id, func):
    """ register a function as the handler for a tracking call type. """
    type_id = int(type_id)
    map[type_id] = func


def get_handler(type_id):
    """ Get handler function for a given tracking call type. """
    type_id = int(type_id)
    try:
        return map[type_id]
    except KeyError:
        raise PixelError('No handler registered for type: {}'.format(type_id))
