from .reduce import reduce

def compose(*functions):
  if not functions:
    return lambda value: value

  if len(functions) == 1:
    return functions[0]

  return reduce(lambda a, b: lambda *arguments: b(a(*arguments)))(functions)
