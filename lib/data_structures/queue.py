from node import * 

# Queue:
#   An abstract data type, otherwise known as a collection, where the
# removal from the front of the collection is called dequeue and the
# addition to the rear of the collection is called enqueue. This
# methodology of operations is called FIFO (First In First Out).

#   Additionally, it is common to have a peek method in this class,
# where the user is able to view the front of the collection without
# modifying the queue.

class Queue:
  def __init__( self ):
    self.head = None
    self.tail = None

  def enqueue( self, data ):
    new_data = Node( data )

    if self.head == None:
      self.head = new_data
      self.tail = new_data

      self.tail.set_next( self.head )
      self.head.set_last( self.tail )
      return self.tail.get_data()
    else:
      current_tail = self.tail
      self.tail = new_data

      self.tail.set_next( current_tail )
      current_tail.set_last( self.tail )
      return self.tail.get_data()

  def peek( self ):
    return self.head.get_data()
  
  def dequeue( self ):
    if self.head == self.tail:
      self.tail = None
      self.head = None
      return None
    else:
      current   = self.head
      self.head = self.head.get_last()
      return current

  def display( self ):
    current = self.head
    count   = 0
    data    = {}

    while current != None:
      data[ count ] = current.get_data()

      count  += 1
      current = current.get_last()
    
    return data

# Double Ended Queue:
#   Same as above, but we also add the ability to add from either
# front or back of the collection.  Same as removal.
class DoubleQueue:
  def __init__( self ):
    self.head = None
    self.tail = None
  
  def peek_front( self ):
    return self.head.get_data()
  
  def peek_rear( self ):
    return self.tail.get_data()

  def add_front( self, data ):
    new_node = Node( data )

    if self.head == None:
      self.head = new_node
      self.tail = new_node

      self.head.set_last( self.tail )
      self.tail.set_next( self.head )

      return self.head.get_data()
    else:
      current   = self.head
      self.head = new_node

      self.head.set_last( current )
      current.set_next( self.head )
      
      return self.head.get_data()

  def enqueue( self, data ):
    new_node = Node( data )

    if self.tail == None:
      self.head = new_node
      self.tail = new_node

      self.head.set_last( self.tail )
      self.last.set_next( self.head )

      return self.tail.get_data()
    else:
      current   = self.tail
      self.tail = new_node

      self.tail.set_next( current )
      current.set_last( self.tail )
      
      return self.tail.get_data()

  def dequeue( self ):
    if self.tail == self.head:
      self.tail = None
      self.head = None
      return None
    else:
      current = self.head
      self.head = self.head.get_last()
      
      current.set_next( None )
      current.set_last( None )

      self.head.set_next( None )
      
      return current.get_data()
  
  def remove_rear( self ):
    if self.tail == self.head:
      self.tail = None
      self.head = None
      return None
    else:
      current = self.tail
      self.tail = self.tail.get_next()

      current.set_next( None )
      current.set_last( None )

      self.tail.set_last( None )
      
      return current.get_data()

  def display( self ):
    count   = 0
    current = self.head
    data    = {}

    while current != None:
      data[ count ] = current.get_data()

      current = current.get_last()
      count  += 1

    return data