from Deque import Deque

class Stack:

  def __init__(self):
    self._dq = Deque()

  def __str__(self):
    return str(self._dq)

  def __len__(self):
    return len(self._dq)

  def push(self, val):
    self._dq.push_back(val)

  def pop(self):
    return self._dq.pop_back()

  def peek(self):
    return self._dq.peek_back()

if __name__ == '__main__':
  stack = Stack()
  print("Test 1: Does Stack operate exclusively in LIFO mode?")
  print("push 2,4,8,9")
  stack.push(2)
  stack.push(4)
  stack.push(8)
  stack.push(9)
  test1a = stack._dq
  print("expected:[ 2, 4, 8, 9 ] actual:", test1a)
  print("pop once")
  stack.pop()
  test1b = stack._dq
  print("expected:[ 2, 4, 8 ] actual:", test1b)
  print("pop again")
  stack.pop()
  test1c = stack._dq
  print("expected:[ 2, 4 ] actual:", test1c)
  print("---------------------------------------------")
  print("Test 2: Does peek operation return correct value and leave the contents of the structures unchanged?")
  sp = stack.peek()
  print("expected: 4 actual:", sp)
  test2 = stack._dq
  print("expected:[ 2, 4 ] actual:", test2)
  print("---------------------------------------------")
  print("Test 3: does Stack implementation return correct length")
  test3 = len(stack._dq)
  print("expected: 2 actual:", test3)
  print("---------------------------------------------")
  print("Test 4: attempt to pop from an empty stack")
  stack.pop()
  stack.pop()
  """empty list"""
  stack.pop()
  test4 = stack._dq
  print("expected: [ ] actual:", test4)
  print("---------------------------------------------")
  print("Test 5: attempt to peek from an empty stack. Does it return None")
  test5 = stack.peek()
  print("expected: None actual:", test5)



