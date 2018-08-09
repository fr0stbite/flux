from flux import apply

from .increment import increment
from .square import square

def test_apply():
  result = apply(2, increment, square)

  assert result == 9
