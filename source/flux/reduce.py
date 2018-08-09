from ._reduce import _reduce

def reduce(function, initializer=None):
  if initializer is None:
    return lambda iterable: _reduce(function, iterable)

  return lambda iterable: _reduce(function, iterable, initializer)
