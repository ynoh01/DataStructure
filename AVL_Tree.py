class AVL_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class
  def __init__(self):
    self._root = None
    # TODO complete initialization

  class _AVL_Node:

    # TODO The Node class is private. You may add any attributes and
    # methods you need.

    def __init__(self, value):
      self._value = value
      self._height = 1
      self._left = None
      self._right = None
      # TODO complete Node initialization

    def find_height(self,t):
        if t is None:
         return 0
        else:
         return 1 + max(self.find_height(t._left), self.find_height(t._right))

    def isBalance(self, t):
        if t is None:
          return 0
        else:
          return (self.find_height(t._right) - self.find_height(t._left))




  def _rotate_left(self,new_root):
    old_root = new_root
    new_root = old_root._right
    old_root._right = new_root._left
    new_root._left = old_root
    old_root._height = old_root.find_height(old_root)
    new_root._height = new_root.find_height(new_root)

    return new_root

  def _rotate_right(self, new_root):
    old_root = new_root
    new_root = old_root._left
    old_root._left = new_root._right
    new_root._right = old_root
    old_root._height = old_root.find_height(old_root)
    new_root._height = new_root.find_height(new_root)

    return new_root


  def re_balance(self,t):
    t._height = t.find_height(t)
    balance = t.isBalance(t)

    if balance == 2 and t._right.isBalance(t._right) >= 0:
        t = self._rotate_left(t)
        return t
    elif balance == 2 and t._right.isBalance(t._right) < 0:
        t._right = self._rotate_right(t._right)
        t = self._rotate_left(t)
        return t
    elif balance == -2 and t._left.isBalance(t._left) <= 0:
        t = self._rotate_right(t)
        return t
    elif balance <= -2 and t._left.isBalance(t._left) > 0:
        t._left = self._rotate_left(t._left)
        t = self._rotate_right(t)
    return t



  def insert_element(self, value):

    self._root = self._insert_help(value,self._root)


  def _insert_help(self, value, t):

    if t is None:
      new_node = self._AVL_Node(value)
      return new_node


    elif t._value > value:
      t._left = self._insert_help(value,t._left)
      t = self.re_balance(t) #check the balance after insertion
      return t


    elif t._value < value:
      t._right = self._insert_help(value,t._right)
      t = self.re_balance(t)
      return t

    elif t._value == value:
        return t




  def remove_element(self, value):
    if self._root is None:
        return
    else:
        self._root = self._remove_help(value,self._root)

  def _remove_help(self, value, t):

    if t._value == value:
       if t._right is not None and t._left is not None:
           t._value = self.isMin(t._right)
           t._right = self._remove_help(t._value,t._right)
           t._height = t.find_height(t)
           return t

       elif t._left is not None or t._right is not None:
         if t._right is not None :
             t._value = self.isMin(t._left)
             t._left = self._remove_help(t._value,t._left)
             t._height = t.find_height(t)
             return t

         else:
             t._value = self.isMin(t._right)
             t._right = self._remove_help(t._value,t._right)
             t._height = t.find_height(t)
             return t


       else:
          return

    elif t._value < value:
        t._right = self._remove_help(value,t._right)
        t._height = t.find_height(t)
        t = self.re_balance(t)
        return t

    elif t._value > value:
        t._left = self._remove_help(value,t._left)
        t._height = t.find_height(t)
        t = self.re_balance(t)
        return t

    elif t is None:
        return None

  def isMin(self,t):

    while t._left is not None:
      t = t._left

    return t._value


  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # TODO replace pass with your implementation

    def _in_order_help(t, result):
        if t is not None:
         result = _in_order_help(t._left, result)
         result += ', ' + str(t._value)
         result = _in_order_help(t._right, result)
        return result

    string = ''
    if self._root is not None:
        string = _in_order_help(self._root, string)
    return '[' + string[1:] + ' ]'



  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.

    def _pre_order_help(t, result):
        if t is not None:
            result += ', ' + str(t._value)
            result = _pre_order_help(t._left, result)
            result = _pre_order_help(t._right, result)
        return result

    string = ''
    if self._root is not None:
        string = _pre_order_help(self._root, string)
    return '[' + string[1:] + ' ]'


  def post_order(self):
    # Construct and return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # TODO replace pass with your implementation

    def _post_order_help(t, result):
        if t is not None:
            result = _post_order_help(t._left, result)
            result = _post_order_help(t._right, result)
            result += ', ' + str(t._value)
        return result

    string = ''
    if self._root is not None:
        string = _post_order_help(self._root, string)
    return '[' + string[1:] + ' ]'


  def get_height(self):
    if self._root is None:
      return 0
    return self._root._height




  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  tree = AVL_Tree()


  print("Test empty tree")
  print("Expected: [ ], Actual:", tree)
  print("Expected height: 0, Actual height:", tree.get_height())
  print("-------------------------------------------------")
  print("Test insertion")
  tree.insert_element(15)
  print("Expected: [ 15 ], Actual:", tree)
  print("Expected height: 1, Actual height:", tree.get_height())
  print("")
  print("Test deletion")
  tree.remove_element(15)
  print("Expected: [ ], Actual:", tree)
  print("Expected height: 0, Actual height:", tree.get_height())
  print("")
  print("Test deletion from empty tree - it should ignore the command")
  print("Expected: [ ], Actual:", tree)
  print("Expected height: 0, Actual height:", tree.get_height())

  print("-------------------------------------------------")
  print("Test re-balance after every operation - testing each rotation methods")
  print("Also testing three traversal methods")
  print("")
  print("test right rotation")
  print("insert 44, 17, 50, 15, 18, 13, 16, 12 and remove 12")
  tree1 = AVL_Tree()
  tree1.insert_element(44)
  tree1.insert_element(17)
  tree1.insert_element(50)
  tree1.insert_element(15)
  tree1.insert_element(18)
  tree1.insert_element(13)
  tree1.insert_element(16)
  tree1.insert_element(12)
  tree1.remove_element(12)

  print("Expected In_order: [ 13, 15, 16, 17, 18, 44, 50 ], Actual:", tree1.in_order())
  print("Expected pre_order: [ 17, 15, 13, 16, 44, 18, 50 ], Actual:", tree1.pre_order())
  print("Expected post_order: [ 13, 16, 15, 18, 50, 44, 17 ], Actual:", tree1.post_order())
  print("Expected height: 3, Actual", tree1.get_height())

  print("")
  print("test left rotation")
  print("insert 17, 13, 20, 18, 25, 23, 27, 29 and remove 29")
  tree2 = AVL_Tree()
  tree2.insert_element(17)
  tree2.insert_element(13)
  tree2.insert_element(20)
  tree2.insert_element(18)
  tree2.insert_element(25)
  tree2.insert_element(23)
  tree2.insert_element(27)
  tree2.insert_element(29)
  tree2.remove_element(29)
  print("Expected In_order: [ 13, 17, 18, 20, 23, 25, 27 ], Actual:", tree2.in_order())
  print("Expected pre_order: [ 20, 17, 13, 18, 25, 23, 27 ],Actual:", tree2.pre_order())
  print("Expected post_order: [ 13, 18, 17, 23, 27, 25, 20 ],Actual:", tree2.post_order())
  print("Expected height: 3, Actual", tree2.get_height())
  print("")

  print("test left-right rotation")
  print("insert 44, 17, 50, 55, 15, 20, 18, 25 and remove 55 ")
  tree3 = AVL_Tree()
  tree3.insert_element(44)
  tree3.insert_element(17)
  tree3.insert_element(50)
  tree3.insert_element(55)
  tree3.remove_element(55)
  tree3.insert_element(15)
  tree3.insert_element(20)
  tree3.insert_element(18)
  tree3.insert_element(25)
  print("Expected In_order: [ 15, 17, 18, 20, 25, 44, 50 ], Actual:", tree3.in_order())
  print("Expected pre_order:[ 20, 17, 15, 18, 44, 25, 50 ], Actual:", tree3.pre_order())
  print("Expected post_order:[ 15, 18, 17, 25, 50, 44, 20 ], Actual:", tree3.post_order())
  print("Expected height: 3, Actual:", tree3.get_height())
  print("")

  print("test right-left rotation")
  print("insert 44, 17, 50, 15, 20, 16, 18, 25 and remove 16")
  tree4 = AVL_Tree()
  tree4.insert_element(44)
  tree4.insert_element(17)
  tree4.insert_element(50)
  tree4.insert_element(15)
  tree4.insert_element(20)
  tree4.insert_element(16)
  tree4.insert_element(18)
  tree4.insert_element(25)
  tree4.remove_element(16)
  print("Expected In_order: [ 15, 17, 18, 20, 25, 44, 50 ], Actual:", tree4.in_order())
  print("Expected pre_order: [ 20, 17, 15, 18, 44, 25, 50 ], Actual:", tree4.pre_order())
  print("Expected post_order: [ 15, 18, 17, 25, 50, 44, 20 ], Actual:", tree4.post_order())
  print("Expected height: 3, Actual:", tree4.get_height())

  print("-------------------------------------------------")
  print("Test tree deletion")
  print("Remove a node with no children is tested above")
  print("")
  print("Remove a node with a one child ")
  print("Insert 5, 2, 18, -4, 3, 21, 19, 25 and remove 18")
  tree5 = AVL_Tree()
  tree5.insert_element(5)
  tree5.insert_element(2)
  tree5.insert_element(18)
  tree5.insert_element(-4)
  tree5.insert_element(3)
  tree5.insert_element(21)
  tree5.insert_element(19)
  tree5.insert_element(25)
  tree5.remove_element(18)
  print("Expected result tree:[ -4, 2, 3, 5, 19, 21, 25 ] , Actual:", tree5)
  print("")

  print("Remove a node with two children")
  print("Insert 12 and 9 to the tree above then remove 12")
  tree5.insert_element(12)
  tree5.insert_element(9)
  tree5.remove_element(12)
  print("Expected result tree:[ -4, 2, 3, 5, 9, 19, 21, 25 ], Actual:", tree5)