class UrlNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = None
        self.prev = None
        

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = UrlNode(homepage)
        self.tail = self.head
        
    def visit(self, url: str) -> None:
        newnode= UrlNode(url)
        self.tail.next = newnode
        newnode.prev = self.tail
        self.tail = newnode

    def back(self, steps: int) -> str:
        while self.tail.prev and steps > 0:
            self.tail = self.tail.prev
            steps-=1
        return self.tail.val



    def forward(self, steps: int) -> str:
        while self.tail.next and steps > 0:
            self.tail = self.tail.next
            steps-=1
        return self.tail.val
        
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)