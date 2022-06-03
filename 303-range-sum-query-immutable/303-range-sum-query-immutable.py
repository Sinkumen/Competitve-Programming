class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = []
        cur = 0
        for n in nums:
            self.arr.append(cur)
            cur += n
        self.arr.append(cur)
            

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right+1] - self.arr[left] 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)