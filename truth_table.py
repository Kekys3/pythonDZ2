from itertools import *
def truth_table(n):
 if n == 0:
  return [()]
 return list(product((0, 1), repeat = n))
print(truth_table(2))