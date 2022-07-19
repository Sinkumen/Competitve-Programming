class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        prev = []
        for i in range(numRows):
            if not prev:
                ans.append([1])
                prev = [1]
                continue
            temp = [1]
            left = 0
            right = 1
            while right < len(prev):
                temp.append(prev[left]+prev[right])
                left += 1
                right += 1
            temp.append(1)
            prev = temp
            ans.append(temp)
        return ans
            