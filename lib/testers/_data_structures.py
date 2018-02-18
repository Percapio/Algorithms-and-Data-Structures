def _singly( _class, _class_name ):
  print 'Performing ' + _class_name + ':'
  linked = _class()

  print 'Performing basic operations.'
  print 'Add at beginning of list.'
  print 'Adding...'
  linked.add(4)
  linked.add(3)
  linked.add(2)
  linked.add(1)
  linked.add(0)

  print 'Attempted to added 4, 3, 2, 1, 0 to linked list.'
  print 'Count if 5 nodes are in linked list...'
  print  str( linked.size() )

  print 'Display full list:' + str( linked.display() )

  print 'Deletion at beginning of list.'
  print 'Deleting...'
  linked.delete()

  print 'Display full list:' + str( linked.display() )

  print 'Search for an element with given key.'
  print 'Searching...'
  print 'key: 2 returns ' + str( linked.search(2) )

  print 'Display full list:' + str( linked.display() )

  print 'Delete an element with given key.'
  print 'Deleting...'
  print 'key: 2'
  linked.remove(2)

  print 'Display full list:' + str( linked.display() )
  
  print 'Insert data into specific key location'
  print 'Inserting...'
  linked.insert(2, 2)

  print 'Display full list:' + str( linked.display() )
  print 'Test Complete'