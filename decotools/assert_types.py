import inspect
from typing import get_origin, get_args, Union

__all__ = ['assert_types']

def _check_type(value, expected) -> bool:
    origin = get_origin(expected)
    args = get_args(expected)

    if origin is Union:
        return any(_check_type(value, arg) for arg in args)

    if origin is list:
        return isinstance(value, list) and all(_check_type(v, args[0]) for v in value)

    if origin is dict:
        key_type, val_type = args
        return isinstance(value, dict) and all(
            _check_type(k, key_type) and _check_type(v, val_type)
            for k, v in value.items()
        )

    if origin is tuple:
        if len(args) == 2 and args[1] is Ellipsis:
            return isinstance(value, tuple) and all(_check_type(v, args[0]) for v in value)
        return isinstance(value, tuple) and len(value) == len(args) and all(
            _check_type(v, t) for v, t in zip(value, args)
        )

    if origin is None:
        return isinstance(value, expected)

    try:
        return isinstance(value, expected)
    except TypeError:
        return False

def assert_types(func):
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs):
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for name, value in bound_args.arguments.items():
            param = sig.parameters[name]
            expected = param.annotation
            if expected is not inspect.Parameter.empty:
                if not _check_type(value, expected):
                    raise TypeError(
                        f"[assert_types] Argument '{name}' = {value!r} does not match with expected type: {expected}"
                    )

        result = func(*args, **kwargs)

        expected_ret = sig.return_annotation
        if expected_ret is not inspect.Signature.empty:
            if not _check_type(result, expected_ret):
                raise TypeError(
                    f"[assert_types] Return {result!r} does not match with expected: {expected_ret}"
                )

        return result

    return wrapper
