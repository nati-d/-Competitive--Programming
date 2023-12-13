class AuthenticationManager:

    def __init__(self, timeToLive: int):
       self.tL = timeToLive
       self.datas = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.datas[tokenId] = currentTime+self.tL
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.datas and self.datas[tokenId] > currentTime:
            self.datas[tokenId] = currentTime+ self.tL

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for key, values in self.datas.items():
            if values > currentTime:
                count+=1
        return count
        
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)