class FreqStack:

    def __init__(self):
        self.maxfreq = defaultdict(int)
        self.freq = defaultdict(list)
        self.max = 0
 
    def push(self, val: int) -> None:
        self.maxfreq[val] += 1
        l  = self.maxfreq[val]
        if l > self.max:
            self.max = l
        self.freq[l].append(val)
        

    def pop(self) -> int:
        top = self.freq[self.max].pop()
        self.maxfreq[top] -= 1
        if not self.freq[self.max]:
            self.max = self.max - 1
        print(top)
        return top
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()