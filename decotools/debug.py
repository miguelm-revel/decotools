def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({", ".join([str(arg) for arg in args])}, {", ".join([str(key) + "=" + str(value) for key, value in kwargs.items()])}) = {result}')
        return result
    return wrapper

