from ._filter import _filter

def filter(function):
  return lambda iterable: _filter(function, iterable)
