def cache(func):
    func_cache = {}
    def wrapper(*args):
        key = frozenset(args)
        if key in func_cache:
            return func_cache[key]
        else:
            func_cache[key] = func(*args)
            return func_cache[key]
    return wrapper

import time
