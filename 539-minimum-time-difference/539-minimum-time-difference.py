class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mins = []
        for time in timePoints:
            hr,mi = time.split(":") 
            minute = int(hr)*60 + int(mi)
            mins.append(minute)
        mins.sort()
        minn = (1440 - mins[-1]) + mins[0]
        for i in range(1,len(mins)):
            minn = min(minn,mins[i]-mins[i-1])
        return minn
            