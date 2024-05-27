from SLLQueue import SLLQueue
from SLLStack import SLLStack
from DLList import DLList
from DLLDeque import DLLDeque
from MaxQueue import MaxQueue
from ChainedHashTable import ChainedHashTable
import random


def test():
  hashTable = ChainedHashTable()
  hashTable.add(83, 'T')
  hashTable.add(26, 'K')
  hashTable.add(79, 'I')
  hashTable.add(16, 'K')
  hashTable.add(57, 'S')
  hashTable.add(64, 'O')
  hashTable.add(90, 'Q')
  hashTable.add(63, 'H')
  hashTable.add(93, 'O')

  hashTable.set(16, 'X')

  print(hashTable)
