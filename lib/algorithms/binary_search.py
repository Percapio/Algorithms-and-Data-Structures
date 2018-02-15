# Binary Search: 
#   Search a sorted array by repeatedly dividing the search interval in 
# half. Begin with an interval covering the whole array. If the value of 
# the search key is less than the item in the middle of the interval, 
# narrow the interval to the lower half. Otherwise narrow it to the upper 
# half. Repeatedly check until the value is found or the interval is empty.
# Return -1 if the target value is not present in the array

######################################################

# Recursive Binary Search
# Time complexity: O( logn )
def recursive( array, target ):
  # The base case, since this binary search is a recursive function
  if len( array ) == 0:
    return -1

  # Grabbing middle value in the array to check if its the target
  mid_index = len( array ) / 2
  mid_value = array[ mid_index ]
  if mid_value == target:
    return mid_index

  # If not, then we divide the array in halves, and recursively call
  # this function base on whether the target value is greater then or
  # less then the the mid value
  if target < mid_value:
    left_array = array[ :mid_index ]
    return recursive( left_array, target )

  else:
    right_array = array[ mid_index + 1: ]
    result = recursive( right_array, target )

    # If reached end, and nothing there, it is -1 all the way home
    if result == -1:
      return -1
    else:
      return result + mid_index + 1

######################################################

######################################################

# Iterative Binary Search
# Time Complexity: O( n )
def iterative( array, target ):
  # location of target
  target_loc = -1

  while( len( array ) > 0 ):
    # grab mid value in array to check if its target
    mid_index = len( array ) / 2
    mid_value = array[ mid_index ]
    if mid_value == target:
      target_loc += mid_index + 1
      return target_loc
    
    # break down the array into parts for while loop to go back
    # through and check for the target
    if target < mid_value:
      array = array[ :mid_index ]
    else:
      target_loc += mid_index + 1
      array = array[ mid_index + 1: ]

  return -1