from Linked_List import Linked_List

class Deque:

  def __init__(self):
    self._list = Linked_List()

  def __str__(self):
    return str(self._list)

  def __len__(self):
    return len(self._list)

  def push_front(self, val):
    if len(self._list)==0:
      self._list.append_element(val)
    else:
      self._list.insert_element_at(val,0)
  
  def pop_front(self):
    return self._list.remove_element_at(0)

  def peek_front(self):
    return self._list.get_element_at(0)


  def push_back(self, val):
    self._list.append_element(val)
  
  def pop_back(self):
    return self._list.remove_element_at(len(self._list)-1)


  def peek_back(self):
    return self._list.get_element_at(len(self._list)-1)


if __name__ == '__main__':
  deque = Deque()
  print(deque)
  print("Test 1: does Deque implementation allow push front and back correctly")
  print("push front 3, 5, 7")
  deque.push_front(3)
  deque.push_front(5)
  deque.push_front(7)
  test1a = deque._list
  print("expected: [ 7, 5, 3 ], actual:", test1a )
  print("push back 8, 9, 10")
  deque.push_back(8)
  deque.push_back(9)
  deque.push_back(10)
  test1b = deque._list
  print("expected: [ 7, 5, 3, 8, 9, 10 ], actual:", test1b )
  print("---------------------------------------------")
  print("Test 2: does Deque implementation allow pop front and back correctly")
  print("pop front")
  deque.pop_front()
  test2a = deque._list
  print("expected: [ 5, 3, 8, 9, 10 ] actual:", test2a )
  print("pop back")
  deque.pop_back()
  test2b = deque._list
  print("expected: [ 5, 3, 8, 9 ] actual:", test2b )
  print("---------------------------------------------")
  print("Test 3: Does Deque implementation allow peek front and back correctly without removing the value")
  print("peek front")
  pf = deque.peek_front()
  print("expected: 5 actual:", pf)
  test3a = deque._list
  print("expected: [ 5, 3, 8, 9 ] actual:", test3a )
  print("peek back")
  pb = deque.peek_back()
  print("expected: 9 actual:", pb)
  test3b = deque._list
  print("expected: [ 5, 3, 8, 9 ] actual:", test3b )
  print("---------------------------------------------")
  print("Test 4: does Deque implementation return correct length")
  test4 = len(deque._list)
  print("expected: 4 actual:", test4)
  print("---------------------------------------------")
  print("Test 5: attempt to pop from an empty deque.")
  deque.pop_back()
  deque.pop_back()
  deque.pop_back()
  deque.pop_back()
  """the deque is empty"""
  print("pop front")
  deque.pop_front()
  test5a = deque._list
  print("expected: [ ] actual:", test5a)
  print("---------------------------------------------")
  print("Test 6: attempt to peek from an empty deque. Does it return None")
  test6a = deque.peek_front()
  print("expected: None actual:", test6a)
  test6b = deque.peek_back()
  print("expected: None actual:", test6b)






