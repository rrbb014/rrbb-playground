
_functions = {}

def register(f):
    _functions[f.__name__] = f
    return f
