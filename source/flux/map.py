from ._map import _map

def map(function):
  return lambda iterable: _map(function, iterable)
