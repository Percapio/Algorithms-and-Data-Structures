def _singly( _class, _class_name ):
  _class linked = new _class()

  print 'Performing basic operations.'
  print 'Insert at beginning of list.'
  print 'Inserting...'
  linked.insert(4)
  linked.insert(3)
  linked.insert(2)
  linked.insert(1)
  linked.insert(0)

  print 'Attempted to added 4, 3, 2, 1, 0 to linked list.'
  print 'Checking if 0 through 4 are in linked list...'

  print '0: ' + str( linked.display_loc(0) )
  print '1: ' + str( linked.display_loc(1) )
  print '2: ' + str( linked.display_loc(2) )
  print '3: ' + str( linked.display_loc(3) )
  print '4: ' + str( linked.display_loc(4) )

  print 'Display full list:' str( linked.display() )

  print 'Deletion at beginning of list.'
  print 'Deleting...'
  linked.delete()

  print 'Checking if first link is not 0...'
  print 'First link is ' + str( linked.display_loc(0) )
  print str( 0 != linked.display_loc(0) )

  print 'Display full list:' str( linked.display() )

  print 'Search for an element with given key.'
  print 'Searching...'
  print 'key: 2 returns ' + str( linked.search(2) )

  print 'Delete an element with given key.'
  print 'Deleting...'
  print 'key: 2'
  linked.remove(2)

  print 'Display full list:' str( linked.display() )
  print 'Test Complete'