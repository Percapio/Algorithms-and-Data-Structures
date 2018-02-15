# Quick Sort:
#   Sort an unsorted array/list by first indexing an element as the pivot point,
# check if this index is our target.  If not, then check if target is more than
# the indexed point. If it is then we check the right half of the list, otherwise
# we check the left half.

######################################################

# Recursive Quick Sort
# Time Complexity: O( nlogn )
def recursive( array ):
  # Recursive requires base case
  size = len( array )

  if size <= 1:
    return array

  # Pivot point to compare elements too
  pivot = array[ 0 ]

  # Left and right list to plug the elements in for sorting
  left  = []
  right = []

  # Iterate: placing lower than in left list and higher in right
  for i in range( 1, size ):
    if array[ i ] < pivot:
      left.append( array[ i ] )
    else:
      right.append( array[ i ] )

  return recursive( left ) + [ pivot ] + recursive( right )  

######################################################

######################################################

# Iterative Quick Sort
# Time Complexity: O( nlogn )
# def iterative( array ):