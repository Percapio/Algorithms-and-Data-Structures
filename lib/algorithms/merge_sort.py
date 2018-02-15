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
  size = len( array )

  # Recursion requires base case
  if size == 1:
    return array

  # Middle index
  midpoint = size / 2

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
  size = len(array)
  i    = 1

  # Iterate, split, sort, merge, flag
  while i < size:

    # The while loop above determines the stepping size for
    # each iteration.  We want to double the stepping size
    # to locate the correct associated index positions for
    # our sub-arrays
    for j in range( 0, size, i + i ):

      # Find our starting and stopping points
      mid_idx = j + i
      right_end = mid_idx + i

      # Grab our sub-arrays to sort
      left  = array[ j:mid_idx ]
      right = array[ mid_idx:right_end ]

      # Don't lose our existing elements
      left_array  = array[ :j ]
      right_array = array[ right_end: ]

      # Call sorting function, and concat all of our arrays
      array = left_array + iter_sort( left, right ) + right_array
    
    # Double again our base stepping size
    i *= 2

  return array

def iter_sort( left, right ):
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
  