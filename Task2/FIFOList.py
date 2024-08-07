class FIFOList:

    _list = []

    def __init__(self, size=10):
        self._size = size

    def push(self, item):
        if len(self._list) >= self._size:
            self._list.pop()

        self._list.insert(0,item)
    
    def pop(self):
        try:
            return self._list.pop()
        except:
            print("FIFOList is empty!")
            return None
    
    def __str__(self):
        return "FIFOList: " + str(self._list)