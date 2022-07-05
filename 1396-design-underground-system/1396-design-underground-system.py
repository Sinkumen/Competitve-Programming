class UndergroundSystem:

    def __init__(self):
        self.ins = {}
        self.total = defaultdict(tuple)
    
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ins[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        cin,time = self.ins[id]
        if cin+"-"+stationName in self.total:
            hours,count = self.total[cin+"-"+stationName]
            self.total[cin+"-"+stationName] = (hours+(t-time),count+1)
        else:
            self.total[cin+"-"+stationName] = ((t-time),1)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        hours,count = self.total[startStation+"-"+endStation]
        return hours/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)