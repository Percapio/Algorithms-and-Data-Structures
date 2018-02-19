from utils import *

def _linked( _class, _class_name ):
  print 'Performing ' + _class_name + ' basic operations:\n'
  linked = _class()

  print 'Add at beginning of list.'  
  for i in range( 4, -1, -1 ):
    print_row( 'Adding...', str( i ) )
    linked.add( i )

  print 'Attempted to added 4, 3, 2, 1, 0 to linked list.'
  print_row( 'Count if 5 nodes are in linked list...', pass_check( linked.size(), 5 ))

  display_data( linked )

  print 'Deletion at beginning of list.'
  linked.delete()
  check = pass_check( linked.display(), {0: 1, 1: 2, 2: 3, 3: 4} )
  print_row( 'Deleting first node...', check )

  display_data( linked )

  print 'Search for an element with given key.'
  check = pass_check( linked.search( 2 ), 3 )
  print_row( 'Searching for key 2...', check )

  display_data( linked )

  print 'Delete an element with given key.'
  check = pass_check( linked.remove( 2 ), True ) 
  print_row( 'Deleting node at key 2...', check )

  display_data( linked )

  print 'Insert data into specific key location'
  check = pass_check( linked.insert( 2, 2 ), {2: 2} )
  print_row( 'Inserting data 2 at key 2...', check )

  display_data( linked )

def _stack( _class, _class_name ):
  print 'Performing ' + _class_name + ' basic operations:\n'
  stack = _class()

  print 'Add to top of stack.'
  for i in range( 4, -1, -1 ):
    print_row( 'Adding...', str( i ) )
    stack.add( i )

  print 'Peek at last node.'
  print_row( 'Peeking...', stack.peek() )

  display_data( stack )

  print 'Delete from top of stack.'
  stack.delete()
  check = pass_check( stack.display(), {0: 1, 1: 2, 2: 3, 3: 4} )
  print_row( 'Deleting first node...', check )

  display_data( stack )

def _queue( _class, _class_name ):
  print 'Performing ' + _class_name + ' basic operations:\n'
  queue = _class()

  print 'Add 4, 3, 2, 1, 0 to back of queue.'
  for i in range( 4, -1, -1 ):
    check = pass_check( queue.enqueue( i ), i )
    print_row( 'Adding...', check )

  print 'Peek at front node.'
  check = queue.peek()
  print_row( 'Peeking...', queue.peek() )
  print_row( 'Returns 4', pass_check( check, 4 ) )

  display_data( queue )

  print 'Delete from front of queue.'
  queue.dequeue()
  check = pass_check( queue.display(), {0: 3, 1: 2, 2: 1, 3: 0} )
  print_row( 'Deleting first node...', check )

  display_data( queue )