# Quick Select:
#   Search an unsorted array/list by finding the nth smallest number
# in an array.  First, we grab a pivot point ( some random el in the array).
# Then we check if this index is our target.  If not, then check if target is more than
# the indexed point. If it is then we check the right half of the list, otherwise
# we check the left half.

######################################################

# Recursive Quick Select
# Time Complexity: O( nlogn )
def recursive( array, target ):
  size = len( array )

  # Recursive, so always gotta have that base case
  if size == 1:
    if array[ 0 ] == target:
      return 1
    else:
      return -1
  
  # Grab our pivot point and check
  pivot     = array[ size - 1]
  if pivot == target:
    return end_point

  # If no go, we do iterate through, sor

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