__all__ = ['pipeable']

class Pipeable:
    def __init__(self, expr):
        self.expr = expr

    def __ror__(self, other):
        return self.expr(other)

    def __rrshift__(self, other):
        return self.expr(other)

    def __call__(self, *args, **kwargs):
        return self.expr(*args, **kwargs)

def pipeable(func):
    return Pipeable(func)
