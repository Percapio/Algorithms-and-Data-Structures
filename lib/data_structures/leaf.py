# Leaf:
#   A node-like data structure which stores references to
# data, a left child, a right child, the unique parent, and
# a unique key which allows for quick searches/sorting.

#  In this Leaf Class, we are going to assume the key and data
# will be given at the instantiation of each leaf.

class Leaf:
  def __init__( self, key, data ):
    self.key    = key
    self.data   = data
    self.left   = None
    self.right  = None
    self.parent = None

  # Get methods
  def get_data( self ):
    return self.data

  def get_left( self ):
    return self.left

  def get_right( self ):
    return self.right
  
  def get_parent( self ):
    return self.parent

  def get_key( self ):
    return self.key

  # Set methods
  def set_data( self, new_data ):
    self.data = new_data
    return self.data

  def set_left( self, node ):
    self.left = node
  
  def set_right( self, node ):
    self.right = node
  
  def set_parent( self, node ):
    self.parent = node

  def set_key( self, key ):
    self.key = key