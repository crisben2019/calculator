from functools import reduce
import re

def sum(*args):
  prog = re.compile(r"(\d+(?:\.\d+)?)")
  arr = filter(lambda item: prog.match(str(item)), args)
  arr = map(lambda x: float(x) if isinstance(x, str) else x, arr)
  return reduce(lambda x,y : x+y, arr, 0)
