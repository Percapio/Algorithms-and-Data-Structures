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