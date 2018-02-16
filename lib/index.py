from algorithms import *

from testers import *

def run_all_functions():
  print '\nCalling all functions.  All results must return true.'
  print 'Search functions:\n'
  # Binary Search
  _algorithms._search( binary_search.recursive, 'Recursive Binary Search' )
  _algorithms._search( binary_search.iterative, 'Iterative Binary Search' )

  # print 'Search n-th smallest number functions:'
  # Quick Select
  # _algorithms._search( quick_select.recursive, 'Recursive Quick Select' )
  # _algorithms._search( quick_select.iterative, 'Iterative Quick Select' )

  print 'Sort functions:\n'
  # Merge Sort
  _algorithms._sort( merge_sort.recursive, 'Recursive Merge Sort' )
  _algorithms._sort( merge_sort.iterative, 'Iterative Merge Sort' )

  # Quick Sort
  _algorithms._sort( quick_sort.recursive, 'Recursive Quick Sort' )
  _algorithms._sort( quick_sort.iterative, 'Iterative Quick Sort' )

if __name__ == "__main__":
  run_all_functions()