# Quick Select:
#   Search an unsorted array/list by finding the nth smallest number
# in an array.  First, we grab a pivot point ( some random el in the array).
# Then we check if this index is our target.  If not, then check if target 
# is more than the indexed point. If it is then we check the right half of 
# the list, otherwise we check the left half.  If its not there, return -1.

######################################################

# Recursive Quick Select
# Time Complexity: O( nlogn )
# def recursive( array, n ):
#   size = len( array )

#   if size <= 1:
#     return array

#   if n in range( 1, 33 ):
#     print 'nth: ' + str( n )

#   array, swapped = partition( array, size - 1, n )

#   step = swapped + 1

#   solution = array[ :step ] + recursive( array[ step: ], n )

#   if type( solution ) is list and len( solution ) == n:
#     print 'solution: ' + str( solution )
#     return [ solution[ 0 ] ]
#   elif type( solution ) is list:
#     print solution
#     return solution
#   else:
#     return [ -1 ]

# def partition( array, end_pos, n ):
#   beg_pos = 0
#   pivot   = array[ beg_pos ]
#   l_mark  = 1
#   r_mark  = end_pos

#   while True:
#     while l_mark < end_pos and array[ l_mark ] < pivot:
#       l_mark += 1
    
#     while r_mark > 0 and array[ r_mark ] > pivot:
#       r_mark -= 1
    
#     if n in range( 1, 33 ):
#       print 'sorted: ' + str( array )
#       print 'r mark: ' + str( r_mark )
#       print 'l mark: ' + str( l_mark )

#     if l_mark > r_mark:
#       if l_mark >= end_pos:
#         break

#       beg_pos += 1
#       pivot    = [ beg_pos ]
#       l_mark   = beg_pos + 1
#       r_mark   = end_pos
    
#     else:
#       array[ beg_pos ], array[ r_mark ] = array[ r_mark ], array[ beg_pos ]
#       array[ r_mark ], array[ l_mark ] = array[ l_mark ], array[ r_mark ]
#       r_mark = end_pos
#       pivot  = array[ l_mark - 1 ]

#   array[ beg_pos ], array[ r_mark ] = array[ r_mark ], array[ beg_pos ]
#   print 'array: ' + str( array )
#   return array, r_mark

######################################################

######################################################

# Iterative Quick Select
# Time Complexity: O( nlogn )
def iterative( array, n ):
  # push the array onto a stack
  stack = array[:]
  size  = len( stack )

  if n > size or n < 1:
    return -1

  # iterate until stack is empty
  while size > 0:
    # decrease stack size, and use size as index for pivot
    size -= 1
    pivot = stack[ size ]

    # partition the given array around the pivot point
    array = partition_iter( array, pivot )
  
  return array[ n ]

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