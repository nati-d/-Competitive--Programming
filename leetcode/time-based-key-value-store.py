class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp,value])
        
        

    def get(self, key: str, timestamp: int) -> str:
        left = -1
        right = len(self.dic[key])
        lst = self.dic[key]
        if self.dic[key]:
            while left+1 < right:
                mid = (left+right)//2
                if lst[mid][0] == timestamp:
                    return lst[mid][1]
                elif lst[mid][0] < timestamp:
                    left = mid
                else:
                    right = mid
            if lst[left][0] > timestamp:
                return ""
            return lst[left][1]
        return ""


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)