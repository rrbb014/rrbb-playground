from common import identity

@identity
def foo():
    return 'bar'

print(foo())
