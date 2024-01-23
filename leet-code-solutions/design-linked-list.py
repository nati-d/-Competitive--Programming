class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        currentNode = self.head
        i = 0

        while currentNode:
            if i == index:
                return currentNode.val
            i += 1
            currentNode = currentNode.next
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        new_node = Node(val)
        cur = self.head
        i = 0

        while cur:
            if i == index - 1:
                new_node.next = cur.next
                cur.next = new_node
                break
            i += 1
            cur = cur.next

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
            return

        i = 0
        cur = self.head

        while cur and cur.next:
            if i == index - 1:
                cur.next = cur.next.next
                break
            i += 1
            cur = cur.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)