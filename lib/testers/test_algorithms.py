import random

### Test Search Function
def f_search( func, func_name ):
  array_of_values = [1,3,5,6,7,9,12,15,16,20,21,22,23,32]

  # Search for true
  rand_num  = random.choice( array_of_values )
  index_num = array_of_values.index( rand_num ) 

  # Search for false
  not_max = max( array_of_values ) + 1
  not_min = 0

  def message( number ):
    return 'Search check for number "' + str( number ) + '" has returned '
  
  checking_message( func_name )

  success1 = func( array_of_values, rand_num ) == index_num
  fail1 = func( array_of_values, not_max ) == -1
  fail2 = func( array_of_values, not_min ) == -1

  print message( rand_num ) + str( success1 )
  print message( not_max ) + str( fail1 )
  print message( not_min ) + str( fail2 ) + '\n'


### Test Sort Functions
def f_sort( func, func_name ):
  array_of_values = [1,3,5,6,7,9,12,15,16,20,21,22,23,32]

  # Scramble array
  copy_of_array = array_of_values[:]
  random.shuffle( copy_of_array )

  def message():
    return 'Sort check "' + str( copy_of_array ) + '" and the outcome was '

  checking_message( func_name )
  success1 = func( copy_of_array ) == array_of_values
  fail1    = func( copy_of_array ) != copy_of_array

  print message() + str( success1 )
  print message() + str( fail1 ) + '\n'


### Utils
def checking_message( func_name ):
  print 'Checking ' + func_name + '...'
