class DynamicArray:
    
    def __init__(self, capacity: int):
        #Initialize a list, in python list can be contiguos block of memory
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        #This is a O(1) operation, which is simply reading from the DynamicArray
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        #This is also a O(1) operation, assuming i is valid.
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:
        val = self.arr[self.length - 1]
        self.length -= 1
        return val
 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        for i in range(self.length):
            newArr[i] = self.arr[i]

        self.arr = newArr

    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
