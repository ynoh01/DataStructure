class Linked_List:
  
  class _Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      
      self._value = val
      self._next = None
      self._previous = None

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    
    
    self._header = Linked_List._Node(None)
    self._trailer = Linked_List._Node(None)
    self._size = 0
    self._header._next = self._trailer
    self._trailer._previous = self._header

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    
    return self._size
    

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the tail position.
    
    new_node = Linked_List._Node(val)
    new_node._next = self._trailer
    new_node._previous = self._trailer._previous
    self._trailer._previous._next = new_node
    self._trailer._previous = new_node
    self._size += 1

  def insert_element_at(self, val, index):
    # assuming the head position is indexed 0, add a
    # node containing val at the specified index. If 
    # the index is not a valid position within the list,
    # ignore the request. This method cannot be used
    # to add an item at the tail position.
    if index >= self._size: 
      return
    new_node = Linked_List._Node(val)
    current = self._header
    for i in range(0, index):
      current = current._next
    new_node._next = current._next
    new_node._previous = current 
    current._next._previous = new_node
    current._next = new_node 
    self._size += 1

  def remove_element_at(self, index):
    # assuming the head position is indexed 0, remove
    # and return the value stored in the node at the 
    # specified index. If the index is invalid, ignore
    # the request.
    if index >= self._size: 
      return    
    if self._size == 0:
      return
    current = self._header
    for i in range(0, index):
      current = current._next 
    current._next = current._next._next
    self._size -= 1
    

  def get_element_at(self, index):
    # assuming the head position is indexed 0, return
    # the value stored in the node at the specified
    # index, but do not unlink it from the list.
    if index >= self._size: 
      return    
    if self._size == 0:
      return    
    current = self._header
    for i in range(0, index+1):
      current = current._next
    return current._value

  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    elements = [None] * self._size 
    current = self._header._next
    i = 0
    while current is not self._trailer:
      elements[i] = str(current._value)
      i += 1
      current = current._next
    return "[" + ",".join(elements)+ "]"
  
class Poly_Val:

  def __init__(self, coef, exp):
    self._coefficient = coef
    self._exponent = exp

  def get_coefficient(self):
    return self._coefficient

  def get_exponent(self):
    return self._exponent

  def __str__(self):
    return str(self._coefficient) + 'x^' + str(self._exponent)

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods ignore your
  # requests when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location?

  linklist = Linked_List()
  
  print ("----------------------")
  print ("test case 1: append correctly to empty list")
  linklist.append_element(1)
  test1 = linklist
  print ("expected:[1]")
  print ("actual:" + str(test1))
  print ("----------------------")

  print ("test case 2: append correctly to non-empty list and change size")
  lenbefore1 = len(linklist)
  linklist.append_element(5)
  test2 = linklist
  print ("expected:[1,5]")
  print ("actual:" + str(test2))
  print ("size before: " + str(lenbefore1))
  print ("expected size after: 2")
  print ("actual size after: " + str(len(linklist)))  
  print ("----------------------")
  
  print ("test case 3: insert correctly to non-empty list and change size")
  lenbefore = len(linklist)
  linklist.insert_element_at(3,1)
  test3 = linklist
  print ("expected:[1,3,5]")
  print ("actual:" + str(test3))
  print ("size before: " + str(lenbefore))
  print ("expected size after: 3")
  print ("actual size after: " + str(len(linklist)))
  print ("----------------------")
  
  print ("test case 4: insert at invalid index")
  linklist1 = Linked_List()
  linklist1.insert_element_at(6,0)
  test4 = linklist1
  print ("expected:[]")
  print ("actual:" + str(test4))
  print ("----------------------")
  
  print ("test case 5: insert at out of range index")
  linklist1.insert_element_at(6,7)
  test5 = linklist1
  print ("expected:[]")
  print ("actual:" + str(test5))
  print ("----------------------")  
  
  print ("test case 6: remove an element correctly")
  print ("remove element at index 2, change size")
  lenbefore3 = len(linklist)
  linklist.append_element(3)
  test61 = linklist
  print ("linked list before:" + str(test61))  
  linklist.remove_element_at(2)
  test6 = linklist
  print ("expected:[1,3,3]")
  print ("actual:" + str(test6))
  print ("size before: " + str(lenbefore3))
  print ("expected size after: 3")
  print ("actual size after: " + str(len(linklist)))  
  print ("----------------------")    
  
  print ("test case 7: remove element at invalid index")
  linklist2 = Linked_List()
  linklist2.remove_element_at(0)
  test7 = linklist2
  print ("expected:[]")
  print ("actual:" + str(test7))
  print ("----------------------")
  
  print ("test case 8: remove element at out of range index")
  linklist.remove_element_at(7)
  test8 = linklist
  print ("expected:[1,3,3]")
  print ("actual:" + str(test8))
  print ("----------------------")   
  
  print ("test case 9: get element correctly")
  test9 = linklist.get_element_at(2) 
  print ("expected:3")
  print ("actual:" + str(test9))
  print ("----------------------")  

  print ("test case 10: get element out of range")
  test10 = linklist.get_element_at(7) 
  print ("expected: None")
  print ("actual: " + str(test10))
  print ("----------------------")  
  
  print("test case 11: print list correctly")
  print ("expected:")
  print ("[1,3,3]")
  print ("actual:") 
  print linklist
  print ("----------------------")  
  
  print ("test case 12: print lists with variety of lengths")
  test = Linked_List()
  test.append_element(1)
  print (test)
  test.append_element(22) 
  print (test)
  test.append_element(555)
  test.append_element(7)
  test.append_element(9)
  print (test)
  test.append_element(36)
  test.append_element(57)
  print (test)
  print ("----------------------")  
  
  print("test case 13: size of empty list")
  linklist4 = Linked_List()
  print ("expected: 0")
  print("actual:" + str(len(linklist4)))
  print ("----------------------")  
  
     
  
  # The following code should appear after your tests for your
  # linked list class.

  p1 = Linked_List()
  p1.append_element(Poly_Val(10,1012))
  p1.append_element(Poly_Val(5,14))
  p1.append_element(Poly_Val(1,0))
  p2 = Linked_List()
  p2.append_element(Poly_Val(3,1990))
  p2.append_element(Poly_Val(-2,14))
  p2.append_element(Poly_Val(11,1))
  p2.append_element(Poly_Val(5,0))
  p3 = Linked_List()
  
  # here, create the Poly_Val objects that should comprise p3
  # and add them to the list. Make sure that p3 is constructed
  # correctly regardless of the contents of p1 and p2. Try
  # building different polynomials for p1 and p2 and ensure that
  # they sum correctly.
 
  j = 0
  for i in range(len(p1)):
    while j < len(p2):
      p1el = p1.get_element_at(i)
      p2el = p2.get_element_at(j)
      p1ex = p1el.get_exponent()      
      p2ex = p2el.get_exponent()
      p2ex = p2el.get_exponent()      
      if p1ex > p2ex:
        p3.append_element(p1el)
        i = i+1
    
      if p1ex < p2ex:
        p3.append_element(p2el)
        j = j+1
        
      if p1ex == p2ex:
        p1coef = p1el.get_coefficient()
        p2coef = p2el.get_coefficient()
        newcoef = p1coef + p2coef
        p3.append_element(Poly_Val(newcoef,p1ex))
        i = i+1
        j = j+1       
  print ("p1: ") 
  print p1
  print ("p2: ")      
  print p2  
  print ("p3: ")      
  print p3
          
  print ("-----------------------")
  print ("polynomial test 1")
  p4 = Linked_List()
  p4.append_element(Poly_Val(6,4789))
  p4.append_element(Poly_Val(7,10))
  p4.append_element(Poly_Val(1,7))
  p4.append_element(Poly_Val(6,-4))
  p1 = p4
  p5 = Linked_List()
  p5.append_element(Poly_Val(8,334))
  p5.append_element(Poly_Val(-3,18))
  p5.append_element(Poly_Val(68,7))
  p5.append_element(Poly_Val(-7,4))
  p5.append_element(Poly_Val(11,-4))  
  p2 = p5
  
  p6 = Linked_List()
  p3 = p6
  
  j = 0
  for i in range(len(p1)):
    while j < len(p2):
      p1el = p1.get_element_at(i)
      p2el = p2.get_element_at(j)
      p1ex = p1el.get_exponent()      
      p2ex = p2el.get_exponent()
      p2ex = p2el.get_exponent()      
      if p1ex > p2ex:
        p3.append_element(p1el)
        i = i+1
    
      if p1ex < p2ex:
        p3.append_element(p2el)
        j = j+1
        
      if p1ex == p2ex:
        p1coef = p1el.get_coefficient()
        p2coef = p2el.get_coefficient()
        newcoef = p1coef + p2coef
        p3.append_element(Poly_Val(newcoef,p1ex))
        i = i+1
        j = j+1       
        
  print ("p1: ") 
  print p1
  print ("p2: ")      
  print p2  
  print ("p3: ")      
  print p3
   