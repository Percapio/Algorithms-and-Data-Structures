from leaf import Leaf

# Binary Tree:
#   A binary tree is data structure designed for more efficient
# sorting/searching of data stored in nodes.  Each binary tree
# starts with a root, or head, that is a node.  The head will
# have at most two chidren nodes, with each child referencing
# at most two children and so on.  ( In this scenario, we will
# call our nodes, leaves, in order to not have compatibility
# issues with our existing node class. )

# Binary Search Tree:
#   This search algorithm checks for a key associated with a
# particular node that contains the value/data.  To quickly
# traverse the tree, the keys have to be sorted with each
# child node ordered in a particular fashion: The left node
# is always a numerical key value that is lower then the
# current key, and the right node is always greater than. The
# methods in our Binary Tree is going to be insert, delete, and
# search.

class BinaryTree:
  def __init__( self ):
    self.root = None

  def insert( self, key, data ):
    leaf = Leaf( key, data )

    if self.root == None:
      self.root = leaf

    else:
      # If tree is not empty, we need to find an empty node
      # at the correct location
      current = self.root
      l_key   = leaf.get_key()
      parent  = current
      c_key   = 0

      while current != None:
        parent = current
        c_key  = current.get_key()

        if l_key < c_key:
          current = current.get_left()

        elif l_key > c_key:
          current = current.get_right()

      # Do not forget to set our parent of the leaf
      current = leaf
      current.set_parent( parent )
      
      # Set child
      if l_key < c_key:
        parent.set_left( current )
      else:
        parent.set_right( current )
  
  def search( self, key ):
    current = self.root

    # Iterate through the leaf by following the weight
    # of the key compared to the node's key
    while current != None:
      c_key = current.get_key()

      if key < c_key:
        current = current.get_left()

      elif key > c_key:
        current = current.get_right()
      
      else:
        return current.get_data()

    return None

  def delete( self, key ):
    current = self.root

    while current != None:
      c_key = current.get_key()

      if key < c_key:
        current = current.get_left()
      
      elif key > c_key:
        current = current.get_right()

      else:
        # Take the smallest value from the right subtree, as this
        # would be the closest successor in value
        right          = current.get_right()
        smallest_right = right

        while smallest_right != None:
          smallest_right = smallest_right.get_left()
        
        # Set parent
        parent = current.get_parent()
        smallest_right.set_parent( parent )

        # Set left and right child
        left         = current.get_left()
        right        = current.get_right()

        smallest_right.set_left( left )
        smallest_right.set_right( right )

        # Set children's parent
        left.set_parent( smallest_right )
        right.set_parent( smallest_right )