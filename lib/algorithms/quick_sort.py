# Quick Sort:
#   Sort an unsorted array/list by first indexing an element as the pivot point,
# check if this index is our target.  If not, then check if target is more than
# the indexed point. If it is then we check the right half of the list, otherwise
# we check the left half.

######################################################

# Recursive Quick Sort
# Time Complexity: O( nlogn )
def recursive( array ):
  size = len( array )

  # Recursive requires base case
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

  # Recursive call this function on left and right and concat
  # results together
  return recursive( left ) + [ pivot ] + recursive( right )  

######################################################

######################################################

# Iterative Quick Sort
# Time Complexity: O( n^2 )
def iterative( array ):
  # Initiate the topmost
  top = len( array ) - 1

  while top >= 0:
    pivot = array[ top ]

    # Make sure to reset our array with sub-arrays concated
    # with the pivot point
    l_left, l_right = sorting( array[ :top ], pivot )
    r_left, r_right = sorting( array[ top+1: ], pivot )

    array = l_left + r_left + [ pivot ] + l_right + r_right

    # Reduce the step by one
    top -= 1

  return array

def sorting( array, pivot ):
  left  = []
  right = []

  if len( array ) == 0:
    return left, right

  for i in range( 0, len(array) ):
    if array[ i ] < pivot:
      left.append( array[ i ] )
    else:
      right.append( array[ i ] )
  
  return left, right