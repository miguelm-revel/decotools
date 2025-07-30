import json

def serialize_to(form):
    if form == 'json':
        dumper = json.dumps
    else:
        raise ValueError('Unknown serialization format')

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return dumper(result)
        return wrapper
    return decorator
