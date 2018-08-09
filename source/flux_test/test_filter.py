from flux import _filter, filter

def test_filter():
  is_odd = lambda x: x % 2 == 1
  value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  assert list(filter(is_odd)(value)) == list(_filter(is_odd, value))
