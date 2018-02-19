from node import *

# Stacks:
#   A stack is an abstract data type that collects elements with
# two principal operations:
#   1. push: adds an element to the top of the collection
#   2. pop:  removes from the top of the collection

#   This particular order of adding and removing from the stack is
# considered LIFO (Last In First Out).  Additional method in stack
# is peek which gives the user access to the top of the stack without
# modifying the stack.

class Stack:
  def __init__( self ):
    self.head = None
  
  def add( self, data ):
    new_head = Node( data )
    new_head.set_next( self.head )
    self.head = new_head
  
  def peek( self ):
    return self.head.get_data()
  
  def delete( self ):
    self.head = self.head.get_next()
    return self.head

  def display( self ):
    current = self.head
    count   = 0
    data    = {}

    while current != None:
      data[ count ] = current.get_data()
      count  += 1
      current = current.get_next()
    
    return data