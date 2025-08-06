def safe(default=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
                return default
        return wrapper
    return decorator

def partial_safe(*exceptions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                print(e)
                return None
        return wrapper
    return decorator

def on_exception(callback):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                return callback()
        return wrapper
    return decorator