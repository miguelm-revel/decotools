__all__ = ['lazy']

class LazyObject:
    def __init__(self, func):
        self.func = func
        self._value = None

    def __repr__(self):
        return '<SymbolicOp>'

    @property
    def value(self):
        if self._value is None:
            self._value = self.func()
        return self._value

    def __add__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() + other.func())
        else:
            return LazyObject(lambda: self.func() + other)
    def __radd__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() + other.func())
        else:
            return LazyObject(lambda: self.func() + other)
    def __sub__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() - other.func())
        else:
            return LazyObject(lambda: self.func() - other)
    def __rsub__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() - other.func())
        else:
            return LazyObject(lambda: self.func() - other)
    def __mul__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() * other.func())
        else:
            return LazyObject(lambda: self.func() * other)
    def __rmul__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() * other.func())
        else:
            return LazyObject(lambda: self.func() * other)
    def __truediv__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() / other.func())
        else:
            return LazyObject(lambda: self.func() / other)
    def __rtruediv__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() / other.func())
        else:
            return LazyObject(lambda: self.func() / other)
    def __floordiv__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() // other.func())
        else:
            return LazyObject(lambda: self.func() // other)
    def __rfloordiv__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() // other.func())
        else:
            return LazyObject(lambda: self.func() // other)
    def __mod__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() % other.func())
        else:
            return LazyObject(lambda: self.func() % other)
    def __rmod__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() % other.func())
        else:
            return LazyObject(lambda: self.func() % other)
    def __pow__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() ** other.func())
        else:
            return LazyObject(lambda: self.func() ** other)
    def __rpow__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() ** other.func())
        else:
            return LazyObject(lambda: self.func() ** other)

def lazy(func):
    def wrapper(*args, **kwargs):
        return LazyObject(lambda: func(*args, **kwargs))
    return wrapper

