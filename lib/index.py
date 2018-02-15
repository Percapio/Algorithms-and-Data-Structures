from algorithms import binary_search
from algorithms import quick_select

from algorithms import merge_sort

from testers import test_funcs

def run_all_functions():
  print '\nCalling all functions.  All results must return true.'
  print 'Search functions:\n'
  # Binary Search
  test_funcs.f_search( binary_search.recursive, 'Recursive Binary Search')
  test_funcs.f_search( binary_search.iterative, 'Iterative Binary Search')

  # Quick Select
  test_funcs.f_search( quick_select.recursive, 'Recursive Quick Select' )
  test_funcs.f_search( quick_select.iterative, 'Iterative Quick Select' )

  print 'Sort functions:\n'
  # Merge Sort
  test_funcs.f_sort( merge_sort.recursive, 'Recursive Merge Sort')
  test_funcs.f_sort( merge_sort.iterative, 'Iterative Merge Sort')

if __name__ == "__main__":
  run_all_functions()