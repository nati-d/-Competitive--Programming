class RandomizedSet:

    def __init__(self):
        self.data = set()
        

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        else:
            self.data.add(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.data:
            self.data.discard(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.data))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()