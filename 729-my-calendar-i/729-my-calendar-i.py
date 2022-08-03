class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for event in self.events:
            if (event[1] > start and event[1] <= end) or (event[0] >= start and event[0] < end) or (event[0] <= start and event[1] > end):
                return False
        self.events.append((start,end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)