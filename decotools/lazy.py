__all__ = ['lazy']

class LazyObject:
    def __init__(self, func, name=None):
        self.func = func
        self.name = name
        self._value = None

    def __repr__(self):
        return f'<SymbolicObject || {self.name}>'

    @property
    def value(self):
        if self._value is None:
            self._value = self.func()
        return self._value

    def __add__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() + other.func(), f'{self.name} + {other.name}')
        else:
            return LazyObject(lambda: self.func() + other, f'{self.name} + {other}')
    def __radd__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() + other.func(), f'{self.name} + {other.name}')
        else:
            return LazyObject(lambda: self.func() + other, f'{self.name} + {other}')
    def __sub__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() - other.func(), f'{self.name} - {other.name}')
        else:
            return LazyObject(lambda: self.func() - other, f'{self.name} - {other}')
    def __rsub__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() - other.func(), f'{self.name} - {other.name}')
        else:
            return LazyObject(lambda: self.func() - other, f'{self.name} - {other}')
    def __mul__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() * other.func(), f'{self.name} * {other.name}')
        else:
            return LazyObject(lambda: self.func() * other, f'{self.name} * {other}')
    def __rmul__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() * other.func(), f'{self.name} * {other.name}')
        else:
            return LazyObject(lambda: self.func() * other, f'{self.name} * {other}')
    def __truediv__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() / other.func(), f'{self.name} / {other.name}')
        else:
            return LazyObject(lambda: self.func() / other, f'{self.name} / {other}')
    def __rtruediv__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() / other.func(), f'{self.name} / {other.name}')
        else:
            return LazyObject(lambda: self.func() / other, f'{self.name} / {other}')
    def __floordiv__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() // other.func(), f'{self.name} // {other.name}')
        else:
            return LazyObject(lambda: self.func() // other, f'{self.name} // {other}')
    def __rfloordiv__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() // other.func(), f'{self.name} // {other.name}')
        else:
            return LazyObject(lambda: self.func() // other, f'{self.name} // {other}')
    def __mod__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() % other.func(), f'{self.name} % {other.name}')
        else:
            return LazyObject(lambda: self.func() % other, f'{self.name} % {other}')
    def __rmod__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() % other.func(), f'{self.name} % {other.name}')
        else:
            return LazyObject(lambda: self.func() % other, f'{self.name} % {other}')
    def __pow__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() ** other.func(), f'{self.name} ** {other.name}')
        else:
            return LazyObject(lambda: self.func() ** other, f'{self.name} ** {other}')
    def __rpow__(self, other):
        if isinstance(other, LazyObject):
            return LazyObject(lambda: self.func() ** other.func(), f'{self.name} ** {other.name}')
        else:
            return LazyObject(lambda: self.func() ** other, f'{self.name} ** {other}')

def lazy(func):
    def wrapper(*args, **kwargs):
        return LazyObject(lambda: func(*args, **kwargs), func.__name__)
    return wrapper


if __name__ == '__main__':
    @lazy
    def obtener_precio():
        print("Consultando API...")
        return 100


    @lazy
    def descuento():
        return 20


    total = obtener_precio() - descuento()
    print(total)  # Imprime: <SymbolicObject ~ obtener_precio - descuento>
    print(total.value)