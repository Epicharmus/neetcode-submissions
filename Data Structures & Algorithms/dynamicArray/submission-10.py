class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None for i in range(capacity)]
        self.length = 0


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        end_item = self.array[self.length]
        self.array[self.length] = None
        return end_item
 
    def resize(self) -> None:
        new_array = [None for i in range(self.capacity*2)]
        for i in range(self.capacity):
            new_array[i] = self.array[i]
            i+=1
        self.array = new_array
        self.capacity = self.capacity*2


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
