from flux import compose

from .increment import increment
from .square import square

def test_compose():
  value = 2

  assert compose(increment, square)(value) == square(increment(value))
