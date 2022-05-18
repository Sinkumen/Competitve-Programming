class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[nums[0]]
        slow = nums[0]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        final = 0
        while nums[slow] != nums[final]:
            final = nums[final]
            slow = nums[slow]
        
        return nums[slow]
        