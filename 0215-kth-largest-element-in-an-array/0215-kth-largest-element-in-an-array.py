class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(arr,k):
            if len(arr) == 1:
                return arr[0]
            
            pivot = random.choice(arr)
            
            greater = [n for n in arr if n > pivot]            
            equal = [n for n in arr if n == pivot]
            less = [n for n in arr if n < pivot]
            
            if k <= len(greater):
                return quickselect(greater,k)
            elif k <= len(greater) + len(equal):
                return pivot
            else:
                j = k - len(greater) - len(equal)
                return quickselect(less,j)
        return quickselect(nums,k)