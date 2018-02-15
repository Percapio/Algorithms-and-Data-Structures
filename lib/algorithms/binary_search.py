#  Binary Search: 
#   Search a sorted array by repeatedly dividing the search interval in 
# half. Begin with an interval covering the whole array. If the value of 
# the search key is less than the item in the middle of the interval, 
# narrow the interval to the lower half. Otherwise narrow it to the upper 
# half. Repeatedly check until the value is found or the interval is empty.


# Recursive Binary Search
# Time complexity: O(logn)
def binary_search_rec( array, target ):
  # The base case, since this binary search is a recursive function
  if len( array ) == 0:
    return 0

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
    return binary_search_rec( left_array, target )
  else:
    right_array = array[ mid_index + 1: ]
    return binary_search_rec( right_array, target ) + mid_index + 1


# Iterative Binary Search
# Time Complexity: O(n)
def binary_search_iter( array, target ):
  # location of target
  target_loc = 0

  while( len( array ) > 0 ):
    # grab mid value in array to check if its target
    mid_index = len( array ) / 2
    mid_value = array[ mid_index ]
    if mid_value == target:
      target += mid_index
    
    # break down the array into parts for while loop to go back
    # through and check for the target
    if target < mid_value:
      array = array[ :mid_index ]
    else:
      target_loc += mid_index + 1
      array = array[ mid_index + 1: ]
  
  print target
  print target_loc
  return target_loc