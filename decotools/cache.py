def cache(func):
    func_cache = {}
    def wrapper(*args, **kwargs):
        args_key = frozenset(args)
        kwargs_key = []
        for k, v in kwargs.items():
            kwargs_key.append((k, v))
        kwargs_key = frozenset(kwargs_key)
        key = (args_key, kwargs_key)
        if key in func_cache:
            return func_cache[key]
        else:
            func_cache[key] = func(*args)
            return func_cache[key]
    return wrapper

import time
