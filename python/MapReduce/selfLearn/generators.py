# link: https://wiki.python.org/moin/Generators
# python documentation link: https://www.python.org/dev/peps/pep-0255/
def first_n_func(n):
  '''
  Builds and return a list.
  This is what we want to be able to do with generators
  Why not just use this? B/c large datasets would take up too much memory.
  Simple example to understand what's happening
  '''
  # 1 liner
  # num, nums = 0, []
  num = 0
  nums = []
  while num < n:
      nums.append(num)
      num += 1
  return nums

var_fnf = first_n_func(100)
# print(var_fnf) # [0,1,2,3...99]
sum_of_var_fnf = sum(var_fnf)
# print(sum_of_var_fnf) # 4950


# Using the generator pattern (an iterable)
class home_grown_generator(object):
  """
  Build a generator ourselves
  """
  def __init__(self, n):
    self.n = n
    self.num = 0

  def __iter__(self):
    return self

  # Python 3 compatibility
  # def __next__(self):
  #    return self.next()

  # Python 2 compatibility
  def next(self):
    if self.num < self.n:
      # 1 liner
      # cur, self.num = self.num, self.num + 1
      cur = self.num
      self.num = self.num + 1
      return cur
    raise StopIteration()

# var_hgg = home_grown_generator(100)
# print(var_hgg) => class object <__main__.home_grown_generator object at 0x7f34a55b4e50>
# print([x for x in var_hgg]) => [0,1,2,3...99]
# sum_of_var_hgg = sum(var_hgg)
# print(sum_of_var_hgg) => 0
# Why 0 and not 4950?
var_hgg = home_grown_generator(10)
for x in var_hgg:
  print(x)
print("generator used up")
for x in var_hgg:
  print(x)
print("nothing in generator")
print(sum(home_grown_generator(10))) # 45


def first_n_gen_func(n):
  """
  a generator that yields items instead of returning a list

  Note that the expression of the number generation logic is clear and natural. 
  It is very similar to the implementation that built a list in memory, 
  but has the memory usage characteristic of the iterator implementation.

  Note: this is perfectly acceptable for expository purposes, but remember
  Python 2:
    first_n_gen_func() = xrange() function,
  Python 3:
    first_n_gen_func() = range() is an immutable sequence type. 
  The built-ins will always be much faster.
  """
  num = 0
  while num < n:
    yield num
    num += 1

# var_fngf = first_n_gen_func(100)
#print(var_fngf) => <generator object first_n_gen_func at 0x7f34a55af8c0>
#print([x for x in var_fngf]) => [0,1,2,3...99]
#sum_of_var_fngf = sum(var_fngf)
#print(sum_of_var_fngf) => 0
#print(sum(first_n_gen_func(100))) => 4950