class Node:
  def __init__(self, value=None, next_node=None, prev_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node
    self.prev_node = prev_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    # a -> b -> c -> d
    # d -> c -> b -> a
    current = self.head
    previous_node = None
    while current is not None: # loop through nodes
      next_node = current.next_node # grab next_node off of current, and store in variable
      current.next_node = previous_node # set current's next_node to previous (flip arrow)
      previous_node = current # sets current's previous node to current (flip arrow)
      current = next_node # sets current to next_node (moves loop to next node value)
      # current.next_node, previous_node, current = previous_node, current, next_node # flip arrow, flip arrow, move to next node
    self.head = previous_node # set new head as former tail (makes the reverse!)

test = LinkedList()
test.add_to_head(1)
test.add_to_head(2)
test.add_to_head(3)
test.add_to_head(4)
test.add_to_head(5)

print(test.head.value)
test.reverse_list()
print(test.head.value)
