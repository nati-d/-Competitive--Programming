class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mins.append(val)
        
    def pop(self) -> None:
        val = self.stack[-1]
        self.stack.pop()
        self.mins.remove(val)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.mins)
       

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()