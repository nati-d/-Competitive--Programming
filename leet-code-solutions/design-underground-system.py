class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}
        self.travel_times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.check_ins[id]
        travel_time = t - check_in_time
        key = (start_station, stationName)
        if key in self.travel_times:
            self.travel_times[key][0] += travel_time 
            self.travel_times[key][1] += 1 
        else:
            self.travel_times[key] = [travel_time, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        total_time, count = self.travel_times[key]
        average_time = total_time / count
        return average_time

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)