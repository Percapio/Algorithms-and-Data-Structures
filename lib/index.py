from algorithms import *
from data_structures import *

from testers import *

def run_all_functions():
  print '\nCalling Algorithm functions.  All results must pass.'
  print 'Search functions:\n'
  print 'Array to test ' + str( [1,3,5,6,7,9,12,15,16,20,21,22,23,32] )
  
  # Binary Search
  _algorithms._search( binary_search.recursive, 'Recursive Binary Search' )
  _algorithms._search( binary_search.iterative, 'Iterative Binary Search' )

  # Quick Select
  # _algorithms._search( quick_select.recursive, 'Recursive Quick Select' )
  _algorithms._search( quick_select.iterative, 'Iterative Quick Select' )

  print 'Sort functions:\n'
  # Merge Sort
  _algorithms._sort( merge_sort.recursive, 'Recursive Merge Sort' )
  _algorithms._sort( merge_sort.iterative, 'Iterative Merge Sort' )

  # Quick Sort
  _algorithms._sort( quick_sort.recursive, 'Recursive Quick Sort' )
  _algorithms._sort( quick_sort.iterative, 'Iterative Quick Sort' )

  print 'Calling Data Structures functions.  Everything must pass.'
  print 'Linked Lists:'
  _data_structures._singly( linked.SinglyList, 'Singly Linked List' )
  _data_structures._singly( linked.DoublyList, 'Doubly Linked List' )


if __name__ == "__main__":
  run_all_functions()