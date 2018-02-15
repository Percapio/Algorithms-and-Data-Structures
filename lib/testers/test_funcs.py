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
    return 'The check for number "' + str( number ) + '" has returned '
  
  print 'Checking ' + func_name + '... all results must return true.'

  success1 = func( array_of_values, rand_num ) == index_num

  fail1 = func( array_of_values, not_max ) == len( array_of_values )

  fail2 = func( array_of_values, not_min ) == 0

  print message( rand_num ) + str( success1 )
  print message( not_max ) + str( fail1 )
  print message( not_min ) + str( fail2 ) + '\n'
