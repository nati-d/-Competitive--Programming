class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.count = 0
        self.dec = deque()
        

    def enQueue(self, value: int) -> bool:
        if self.count < self.k:
            self.count+=1
            self.dec.append(value)
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if self.count > 0:
            self.count-=1
            self.dec.popleft()
            return True
        else:
            return False
        
        

    def Front(self) -> int:
        if self.dec:
            return self.dec[0]
        else:
            return -1
        

    def Rear(self) -> int:
        if self.dec:
            return self.dec[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.count == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()