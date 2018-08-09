from ._filter import _filter
from ._map import _map
from ._reduce import _reduce
from .apply import apply
from .compose import compose
from .filter import filter
from .map import map
from .reduce import reduce

__title__ = 'flux'
__version__ = '1.0.0'
__author__ = 'Tomáš Rottenberg'
__description__ = 'Minimal foundation of core functional concepts and utilities.'
__license__ = 'MIT'
__url__ = 'https://github.com/architectio/architect#readme'
__packages__ = [
  'flux'
]

__all__ = [
  '_filter',
  '_map',
  '_reduce',
  'apply',
  'compose',
  'filter',
  'map',
  'reduce'
]
