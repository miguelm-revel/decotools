def once(func):
    executed = False
    def wrapper(*args, **kwargs):
        nonlocal executed
        if not executed:
            executed = True
            return func(*args, **kwargs)
        else:
            return None
    return wrapper

def retry(n, *exceptions):
    if len(exceptions) == 0:
        exceptions = (Exception,)
    def decorator(func):
        def wrapper(*args, **kwargs):
            e = None
            for i in range(n):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    pass
            else:
                raise e
        return wrapper
    return decorator

def n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator