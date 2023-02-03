class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        self.total = 0
        for i in range(len(w)):
            self.total += w[i]
            self.arr.append(self.total)
        
    def pickIndex(self) -> int:
        rand = random.randint(1,self.total)
        left = 0
        right = len(self.arr)
        ans = 0
        while left <= right:
            mid = (left + right)//2
            if rand > self.arr[mid]:
                left = mid + 1
            else:
                ans = mid
                right = mid-1
        return ans
                


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()