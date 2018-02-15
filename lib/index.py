from algorithms import binary_search
from algorithms import quick_select

from testers import test_funcs

def run_all_functions():
  print 'Search functions:\n'
  # Binary Search
  test_funcs.f_search( binary_search.recursive, 'Recursive Binary Search')
  test_funcs.f_search( binary_search.iterative, 'Iterative Binary Search')

  # Quick Select
  test_funcs.f_search( quick_select.recursive, 'Recursive Quick Select' )
  test_funcs.f_search( quick_select.iterative, 'Iterative Quick Select' )

if __name__ == "__main__":
  run_all_functions()