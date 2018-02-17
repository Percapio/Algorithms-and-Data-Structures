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

  # Partition the array for sorting
  left, right, pivot = partition( array, size )

  # Recursive call this function on left and right and concat
  # results together
  return recursive( left ) + [ pivot ] + recursive( right )  

def partition( array, size ):
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

  return left, right, pivot

######################################################

######################################################

# Iterative Quick Sort
# Time Complexity: O( n^2 )
def iterative( array ):
  # push the array onto a stack
  stack = array[:]
  size  = len( stack )

  # iterate until stack is empty
  while size > 0:
    # decrease stack size, and use size as index for pivot
    size -= 1
    pivot = stack[ size ]

    # partition the given array around the pivot point
    array = partition_iter( array, pivot )
  
  return array

def partition_iter( array, pivot ):
  left  = []
  right = []

  # step through the array, and partition based on 
  for i in range( len(array) ):
    if array[ i ] < pivot:
      left.append( array[ i ] )
    else:
      right.append( array[ i ] )
  
  # concat
  return left + right