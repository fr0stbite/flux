from .compose import compose

def apply(value, *functions):
  return compose(*functions)(value)
