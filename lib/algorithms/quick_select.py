# Quick Select:
#   Search an unsorted array/list by finding the nth smallest number
# in an array.  First, we grab a pivot point ( some random el in the array).
# Then we check if this index is our target.  If not, then check if target is more than
# the indexed point. If it is then we check the right half of the list, otherwise
# we check the left half.  If its not there, return -1.

######################################################

# Recursive Quick Select
# Time Complexity: O( nlogn )
def recursive( array, n ):
  end_pos = len( array ) - 1

  if end_pos <= 1:
    return array

  r_index, array = partition( array, n )

  position = r_index + 1

  if position == n:
    return array[ r_index ]
  elif n < position:
    return recursive( array[ 0:r_index ], n )
  elif n > position:
    return recursive( array[ position: ], n )
  else:
    return -1

def partition( array, n ):
  size  = len( array )
  pivot = array[ size - 1 ]

  left   = []
  right  = []
  r_mark = 0

  for i in range( size ):
    if array[ i ] < pivot:
      left.append( array[ i ] )
      
      if len( array ) == n:
        r_mark = i

    else:
      right.append( array[ i ] )
  
  return r_mark, array

######################################################

######################################################

# Iterative Quick Select
# Time Complexity: O( n )
def iterative( array, target ):
  target_loc = 0

  while len( array ) > 0:
    # Grab pivot point and check
    pivot    = len( array ) / 2
    pivot_el = array[ pivot ]
    if pivot_el == target:
      target_loc += pivot
      return target_loc
    
    # Else, split array in half and check if target is in lower or greater half
    # of array and step through our next iteration of searching
    if target < pivot_el:
      array = array[ :pivot ]
    else:
      target_loc += pivot + 1
      array = array[ pivot + 1: ]
  
  return target_loc