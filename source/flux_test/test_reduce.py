from flux import _reduce, reduce

from .add import add

def test_reduce():
  value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  initializer = 10

  assert reduce(add)(value) == _reduce(add, value)
  assert reduce(add, initializer=initializer)(value) == _reduce(add, value, initializer)
