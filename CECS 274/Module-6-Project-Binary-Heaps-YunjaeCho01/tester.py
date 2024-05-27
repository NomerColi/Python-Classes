from SLLQueue import SLLQueue
from SLLStack import SLLStack
from DLList import DLList
from DLLDeque import DLLDeque
from MaxQueue import MaxQueue
import random
from BinaryHeap import BinaryHeap


def BinaryHeapTest():
  print("Testing BinaryHeap...")
  bh = BinaryHeap()
  #for i in range(10):
  #  bh.add(i)4 6 12 9 17 18 13 20 13 31
  bh.add(4)
  bh.add(6)
  bh.add(12)
  bh.add(9)
  bh.add(17)
  bh.add(18)
  bh.add(13)
  bh.add(20)
  bh.add(13)
  bh.add(31)
  print(bh)
  bh.remove()
  print(bh)
  bh.remove()
  print(bh)


def test():
  BinaryHeapTest()
