class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens = 0
        for n in nums:
            if n%2==0:
                evens += n
        ans = []
        for new,idx in queries:
            prev = nums[idx]
            if nums[idx] % 2 == 0:
                evens -= prev
            nums[idx] += new
            if nums[idx]%2 == 0:
                evens += nums[idx]
            ans.append(evens)

        return ans
            