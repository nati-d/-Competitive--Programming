class Robot:

    def __init__(self, width: int, height: int):
        self.obstacles = set([(width, 0),(width - 1, height),(-1, height - 1),(0, -1)])
        self.current = 0
        self.directions = [(1,0),(0,1),(-1,0),(0,-1)]
        self.dxn = ["East", "North", "West", "South"]
        self.x, self.y = 0, 0
        self.perimeter = 2 * (width + height - 2)
        self.flag = False
        
        

    def step(self, num: int) -> None:
        self.flag = True
        num %= self.perimeter
        dx, dy = self.directions[self.current]
        for _ in range(num):
            if (self.x + dx, self.y + dy) in self.obstacles:
                self.current = (self.current + 1) % 4 
            dx, dy = self.directions[self.current]           
            self.x += dx
            self.y += dy

    def getPos(self) -> List[int]:
        return [self.x, self.y]        

    def getDir(self) -> str: 
        if self.flag and (self.x, self.y) == (0,0):
            self.current = 3       
        return self.dxn[self.current]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
