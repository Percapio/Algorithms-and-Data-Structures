import random

### Utils
def message( _type, _input ):
  return _type + ' check for "' + str( _input ) + '"... '


def checking_message( func_name ):
  print 'Checking ' + func_name + '...'

def random_array():
  array_of_values = [1,3,5,6,7,9,12,15,16,20,21,22,23,32]

  # Scramble array
  shuffled_array = array_of_values[:]
  random.shuffle( shuffled_array )

  return array_of_values, shuffled_array

def target_array( array_of_values ):
  # Search for true
  rand_num  = random.choice( array_of_values )
  index_num = array_of_values.index( rand_num ) 

  # Search for false
  not_max = max( array_of_values ) + 1
  not_min = 0

  return rand_num, index_num, not_max, not_min

def print_row( left, right ):
  print '%-65s %31s' %( left, right )

def pass_check( method, target ):
  return is_true( method == target )

def is_true( boolean ):
  if boolean == True:
    return 'Pass'
  else:
    return 'Fail'

def display_data( data ):
  print_row( 'Display all data:', str( data.display() ))
  print ''
