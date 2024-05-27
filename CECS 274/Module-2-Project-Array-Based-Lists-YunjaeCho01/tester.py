from ArrayList import ArrayList
from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack
import random


def ArrayStackTest():
  stack = ArrayStack()
  print("Created empty stack.")
  for i in range(1, 11):
    stack.push(i)
  #for i in range(1, 11):
  #  stack.pop()
  print(f"stack: {stack} a: {stack.a}")
  stack.remove(1)
  print(f"stack: {stack} a: {stack.a}")


def ArrayQueueTest():
  queue = ArrayQueue()
  print("Created empty queue.")
  for i in range(1, 17):
    queue.add(i)
  for i in range(1, 11):
    queue.remove()
  print(f"j = {queue.j} queue:{queue} backarray:{queue.a}")
  queue.remove()
  print(queue)


def ArrayListTest():
  list = ArrayList()
  for i in range(9):
    list.append(i + 1)
  list.remove(4)
  print(f"j = {list.j} list:{list} backarray:{list.a}")


def test():
  """write your own tester in this function"""

  option = input("1. ArrayStack, 2. ArrayQueue, 3. ArrayList\n")
  if option == "1":
    ArrayStackTest()
  elif option == "2":
    ArrayQueueTest()
  elif option == "3":
    ArrayListTest()
