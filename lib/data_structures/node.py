#   A Node Class contains data, as well as a reference to
# the next Node.  Then we create the methods necessary for
# a basic Node, which includes, get data, get next, set data,
# and set next.

class Node:
  def __init__( self, initial_data ):
    self.data = initial_data
    self.next = None

    #   For Backward Traversal compatibility, we add a
    # reference to the last node
    self.last = None
  
  def get_data( self ):
    return self.data

  def get_next( self ):
    return self.next

  def set_data( self, new_data ):
    self.data = new_data

  def set_next( self, new_next ):
    self.next = new_next

  #   For Backward Traversal compatibility, we add last 
  # lookup and set methods
  def get_last( self ):
    return self.last

  def set_last( self, new_last ):
    self.last = new_last