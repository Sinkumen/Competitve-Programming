class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        stack = [nums[0]]
        reverse = [nums[-1]]
        life = 1
        for i in range(1,len(nums)):
            if nums[i] < stack[-1]:
                if life:
                    stack.append(stack[-1])
                    life -= 1 
                else:
                    break
            else:
                stack.append(nums[i])
        life = 1
        for j in range(len(nums)-2,-1,-1):
            if nums[j] > reverse[-1]:
                if life:
                    reverse.append(reverse[-1])
                    life -= 1 
                else:
                    break
            else:
                reverse.append(nums[j])

        return len(stack) == len(nums) or len(reverse) == len(nums)
                