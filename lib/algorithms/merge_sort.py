# Merge Sort:
# Sort an unsorted array by first declaring a halfway point and then
# splitting the arrays into two parts.  Recursiviely doing so until
# there is only one element in each array.  After, perform a iterative
# sort by comparing the one value in each array against a value in 
# the other array

######################################################

# Recursive Merge Sort
# Time Complexity: O( nlogn )
def recursive( array ):
  # Recursion requires base case
  if len( array ) == 1:
    return array

  # Middle index
  midpoint = len( array ) / 2

  # split array
  left_array  = array[ :midpoint ]
  right_array = array[ midpoint: ]

  # Recursive call
  left  = recursive( left_array )
  right = recursive( right_array )

  # Sort two arrays against each other, than return
  return rec_sort( left, right )

def rec_sort( left, right ):
  results = []

  # iterate until one of the two arrays runs out
  while len( left ) > 0 and len( right ) > 0:

    # check which value within each array is lower
    # append to results and remove from current array
    if left[ 0 ] <= right[ 0 ]:
      shift_left = left[ 0 ]
      left       = left[ 1: ]
      results.append( shift_left )
    else:
      shift_right = right[ 0 ]
      right       = right[ 1: ]
      results.append( shift_right )
  
  # return all arrays concated
  return results + left + right

######################################################

######################################################

# Iterative Merge Sort
# Time Complexity: O( nlogn )
def iterative( array ):
  # Flag to let us know when we're done
  not_sorted = True
  gp  = 1
  idx = 0

  # Iterate, split, sort, merge, flag
  for gp in range( 1, len(array), gp*2 ):
    for idx in range( 0, len(array), idx+2 ):
      left  = array[ :idx]
      right = array[ idx: ]

      # Sorting function
      # if at any point the right side of the array had to
      # be shift before the left, we have to go through
      # the loop again
      array, not_sorted = iter_sort( left, right )

  return array

def iter_sort( left, right ):
  results = []

  # Mini flag to check if all values in left array is
  # lower than all values of right array, and sorted
  not_sorted = False

  # iterate until one of the two arrays runs out
  while len( left ) > 0 and len( right ) > 0:

    # check which value within each array is lower
    # append to results and remove from current array
    if left[ 0 ] <= right[ 0 ]:
      shift_left = left[ 0 ]
      left       = left[ 1: ]
      results.append( shift_left )
    else:
      shift_right = right[ 0 ]
      right       = right[ 1: ]
      not_sorted  = True
      results.append( shift_right )

  # return all arrays concated
  return results + left + right, not_sorted
  