class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        start = 0
        end = len(self.map[key])-1
        ans = ""
        while start <= end:
            mid = (start+end)//2
            if self.map[key][mid][0] == timestamp:
                return self.map[key][mid][1]
            elif self.map[key][mid][0] < timestamp:
                ans = self.map[key][mid][1]
                start = mid + 1
            else:
                end = mid - 1
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)