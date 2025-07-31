def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({", ".join([str(arg) for arg in args])}, {", ".join([str(key) + "=" + str(value) for key, value in kwargs.items()])}) = {result}')
        return result
    return wrapper

def count_calls(func):
    func.call_no = 0
    def wrapper(*args, **kwargs):
        func.call_no += 1
        return func(*args, **kwargs)
    return wrapper