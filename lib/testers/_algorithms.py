from utils import *

### TEST Search Function
def _search( func, func_name ):
  # Initiate array and target values
  array_of_values, shuffled_array = random_array()
  rand_num, index_num, not_max, not_min = target_array( array_of_values )

  # Either Binary or Quick Select
  success1 = ''
  fail1    = ''
  fail2    = ''

  if func_name == 'Recursive Binary Search' or func_name == 'Iterative Binary Search':
    success1 = func( array_of_values, rand_num ) == index_num
    fail1    = func( array_of_values, not_max )  == -1
    fail2    = func( array_of_values, not_min )  == -1

  elif func_name == 'Recursive Quick Select' or func_name == 'Iterative Quick Select':
    success1 = func( shuffled_array, index_num ) == rand_num
    fail1    = func( shuffled_array, not_max )   == -1
    fail2    = func( shuffled_array, not_min )   == -1
  
  # Check if numbers in, and not in, all return true, and messages
  checking_message( func_name )

  print message( 'Search', rand_num ) + str( success1 )
  print message( 'Search', not_max ) + str( fail1 )  
  print message( 'Search', not_min ) + str( fail2 ) + '\n'


### TEST Sort Functions
def _sort( func, func_name ):
  # Initate array and scrambled array
  array_of_values, shuffled_array = random_array()

  # Outgoing messages
  checking_message( func_name )

  # Check if sorted and unsorted to return true, and messages
  success1 = func( shuffled_array ) == array_of_values
  print message( 'Sort', shuffled_array ) + str( success1 )

  fail1    = func( shuffled_array ) != shuffled_array
  print message( 'Sort', shuffled_array ) + str( fail1 ) + '\n'