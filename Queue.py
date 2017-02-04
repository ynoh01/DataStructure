from Deque import Deque

class Queue:

  def __init__(self):
    self._dq = Deque()

  def __str__(self):
    return str(self._dq)

  def __len__(self):
    return len(self._dq)

  def enqueue(self, val):
    self._dq.push_back(val)

  def dequeue(self):
    return self._dq.pop_front()


if __name__ == '__main__':
  que = Queue()
  print("Test 1: Does your Queue operate exclusively in FIFO mode? ")
  print("enqueue 3,6,9,8")
  que.enqueue(3)
  que.enqueue(6)
  que.enqueue(9)
  que.enqueue(8)
  test1a = que._dq
  print("expected: [ 3, 6, 9, 8 ] actual:", test1a)
  print("dequeue once")
  que.dequeue()
  test1b = que._dq
  print("expected: [ 6, 9, 8 ] actual:", test1b)
  print("dequeue again")
  que.dequeue()
  test1c = que._dq
  print("expected: [ 9, 8 ] actual:", test1c)
  print("---------------------------------------------")
  print("Test 2: does Queue implementation return correct length")
  test2 = len(que._dq)
  print("expected: 2 actual:", test2)
  print("---------------------------------------------")
  print("Test 3: attempt to dequeue from an empty queue")
  que.dequeue()
  que.dequeue()
  """empty queue"""
  que.dequeue()
  test3 = que.dequeue()
  print("expected: None actual:", test3)


