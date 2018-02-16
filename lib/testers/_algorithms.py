from utils import *

### TEST Search Function
def _search( func, func_name ):
  # Initiate array and target values
  array_of_values, shuffled_array = random_array()
  rand_num, index_num, not_max, not_min = target_array( array_of_values )

  # Either Binary or Quick Select
  input_array = ''
  input_value = ''

  if func_name == 'Recursive Binary Search' or func_name == 'Iterative Binary Search':
    input_array = array_of_values
    input_value = rand_num

  elif func_name == 'Recursive Quick Select' or func_name == 'Iterative Quick Select':
    input_array  = shuffled_array
    input_value  = index_num + 1
  
  # Check if numbers in, and not in, all return true, and messages
  checking_message( func_name )

  success1 = func( input_array, input_value ) == index_num
  print message( 'Search', rand_num ) + str( success1 )

  fail1    = func( input_array, not_max )     == -1
  print message( 'Search', not_max ) + str( fail1 )
  
  fail2    = func( input_array, not_min )     == -1
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