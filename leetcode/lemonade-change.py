class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0

        
        for i in range(len(bills)):
            if bills[i] == 5:
                count5+=1
            elif bills[i] == 10:
                if count5 < 1:
                    return False
                count5-=1
                count10+=1
            else:
                if count10 >= 1 and count5 >= 1:
                    count10 -=1
                    count5 -=1
                elif not count10 and count5 > 2:
                    count5 -=3
                else:
                    return False
           
        return True
        