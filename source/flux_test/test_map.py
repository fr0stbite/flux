from flux import _map, map

from .increment import increment

def test_map():
  value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  assert list(map(increment)(value)) == list(_map(increment, value))
