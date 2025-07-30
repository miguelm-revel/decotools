import os


def inject_globals(func):
    args = func.__code__.co_varnames[:func.__code__.co_argcount]
    def wrapper(**kwargs):
        for arg in args:
            if arg not in kwargs or kwargs[arg] is None:
                kwargs[arg] = os.getenv(arg)

        return func(**kwargs)
    return wrapper

