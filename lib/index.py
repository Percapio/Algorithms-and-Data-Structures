from algorithms import *

from testers import *

def run_all_functions():
  print '\nCalling all functions.  All results must return true.'
  print 'Search functions:\n'
  # Binary Search
  test_algorithms.f_search( binary_search.recursive, 'Recursive Binary Search' )
  test_algorithms.f_search( binary_search.iterative, 'Iterative Binary Search' )

  # print 'Search n-th smallest number functions:'
  # Quick Select
  # test_algorithms.f_search( quick_select.recursive, 'Recursive Quick Select' )
  # test_algorithms.f_search( quick_select.iterative, 'Iterative Quick Select' )

  print 'Sort functions:\n'
  # Merge Sort
  test_algorithms.f_sort( merge_sort.recursive, 'Recursive Merge Sort' )
  test_algorithms.f_sort( merge_sort.iterative, 'Iterative Merge Sort' )

  # Quick Sort
  test_algorithms.f_sort( quick_sort.recursive, 'Recursive Quick Sort' )

if __name__ == "__main__":
  run_all_functions()