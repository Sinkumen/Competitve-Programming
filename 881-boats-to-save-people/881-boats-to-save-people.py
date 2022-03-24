class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        left = 0
        right = len(people)-1
        while left <= right:
            summ = people[left] + people[right]
            ans += 1
            if summ <= limit:
                left += 1
            right -= 1
            
        return ans
        
                
                
            