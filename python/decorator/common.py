def identity(f):
    return f
    
_functions = {}

def register(f):
    _functions[f.__name__] = f
    return f
