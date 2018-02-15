# Quick Select:
#   Search a sorted array/list by first indexing an element as the pivot point,
# check if this index is our target.  If not, then check if target is more than
# the indexed point. If it is then we check the right half of the list, otherwise
# we check the left half.

# Recursive Quick Select
# Time Complexity: O( logn )
def recursive( array, target ):
  # Recursive, so always gotta have that base case
  if len( array ) == 0:
    return 0
  
  # Grab our pivot point and check
  pivot    = len( array ) / 2
  pivot_el = array[ pivot ]
  if pivot_el == target:
    return pivot

  # If no go, we do our recursion by check whether the target value is either
  # in the greater half of the list or the lower half based on whether the
  # target value is more or less than pivot_el
  if target < pivot_el:
    left_array = array[ :pivot ]
    return recursive( left_array, target )
  else:
    right_array = array[ pivot + 1: ]
    return recursive( right_array, target ) + 1 + pivot


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