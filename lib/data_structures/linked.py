# Linked Lists:
#   An ordered set of data elements, each containing a 
# link to its successor (and sometimes its predecessor).

#   For a Singly Linked List, we create a Node Class which 
# contains the data and it holds a reference to the next
# Node.  Then we create the methods necessary for a basic
# Node, which includes, get data, get next, set data, and
# set next.

class Node:
  def __init__( self, initial_data ):
    self.data = initial_data
    self.next = None

    #   For Doubly Linked List, we add last to allow for
    # backward traversal.
    self.last = None
  
  def get_data( self ):
    return self.data

  def get_next( self ):
    return self.next

  def set_data( self, new_data ):
    self.data = new_data

  def set_next( self, new_next ):
    self.next = new_next

  #   For Doubly Linked List, we add last methods to allow
  # for traversal.
  def get_last( self ):
    return self.last

  def set_last( self, new_last ):
    self.last = new_last

#   Next, we create a Singly Class that will create, point,
# display, delete, and remove the Nodes in a single list.
# A Singly List can only perform all of the above functions
# in a single direction.

class SinglyList:
  def __init__( self ):
    self.head = None

  def is_empty( self ):
    return self.head == None

  def add( self, data ):
    # Create and point to a new node
    new_head = Node( data )

    # This node's next references the current head
    new_head.set_next( self.head )

    # Set current head to the new node
    self.head = new_head

  def size( self ):
    # Point to current head
    current = self.head

    # Set a counter
    count   = 0

    # Iterate until Null / None
    while current != None:
      count += 1

      # Point to the next node
      current = current.get_next()
    
    return count

  def display( self ):
    current  = self.head
    count    = 0
    all_data = {}

    while current != None:
      all_data[ count ] = current.get_data()

      count   += 1
      current  = current.get_next()
    
    return all_data

  def delete( self ):
    # Point head to head's next
    if self.is_empty():
      return 'Error: List is empty.'
    else:
      self.head = self.head.get_next()
      return self.head

  def search( self, key ):
    current = self.head
    count   = 0

    while current != None:
      if count == key:
        return current.get_data()

      count  += 1
      current = current.get_next()

    return 'No data present for key.'
  
  def remove( self, key ):
    # Point to current head
    current = self.head
    count   = 0

    # Iterate until Null / None
    while current != None:
      # Iterate key
      count += 1

      # If next counter is key, then set temp
      # pointer to next Node's node, and point
      # current Node to that node
      if count == key:
        temp = current.get_next().get_next()

        current.set_next( temp )
        
        return True

      current = current.get_next()

    return False

  def insert( self, key, data ):
    current = self.head
    count   = 0

    while current != None:
      if count == key:
        # Create a new node
        new_node = Node( data )

        # Point new node to next node
        new_node.set_next( current.get_next() )

        # Point current node to this node
        current.set_next( new_node )

        return { count: new_node.get_data() }
      
      count += 1

    return False

class DoublyList:
  def __init__( self ):
    self.head = None
  
  def is_empty( self ):
    return self.head == None

  def add( self, new_data ):
    new_head  = Node( new_data )
    new_head.set_next( self.head )

    if self.head != None:
      self.head.set_last( new_head )
      
    self.head = new_head

  def size( self ):
    current = self.head
    count   = 0

    while current != None: 
      count  += 1
      current = current.get_next()
    
    return count

  def display( self ):
    current = self.head
    count   = 0 
    ouput   = {}

    while current != None:
      ouput[ count ] = current.data 
      count  += 1
      current = current.get_next()
    
    return ouput
  
  def delete( self ):
    current   = self.head
    self.head = current.get_next()
    return self.head
  
  def search( self, key ):
    current = self.head
    count   = 0

    while current != None:
      if count == key:
        return current.get_data()
      
      count += 1
      current = current.get_next()
    
    return False

  def remove( self, key ):
    current = self.head
    count   = 0

    while current != None:
      if count == key:
        next_node = current.get_next()
        last_node = current.get_last()

        next_node.set_last( last_node )
        last_node.set_next( next_node )

        return True
      
      count += 1
      current = current.get_next()
    
    return False

  def insert( self, key, data ):
    current = self.head
    count   = 0

    while current != None:
      count += 1

      if count == key:
        next_node = current
        last_node = current.get_last()

        current   = Node( data )
        current.set_next( next_node )
        current.set_last( last_node )

        next_node.set_last( current )
        last_node.set_next( current )

        return { key: current.get_data() }
    
    return 'Failed to insert data.'