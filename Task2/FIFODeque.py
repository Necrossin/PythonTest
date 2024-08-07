from collections import deque

class FIFODeque:

    def __init__(self, size=10):
        self._list = deque( [], size)

    def push(self, item):
        self._list.appendleft(item)

    def pop(self):
        try:
            return self._list.pop()
        except:
            print("FIFODeque is empty!")
            return None
    
    def __str__(self):
        return "FIFODeque: " + str(self._list)