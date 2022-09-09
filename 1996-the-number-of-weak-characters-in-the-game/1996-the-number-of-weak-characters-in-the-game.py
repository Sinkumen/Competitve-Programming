class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        N = len(properties)
        properties.sort()
        # print(properties)
        suff = []
        curMax = 0
        attack = 0
        for i in range(N-1,-1,-1):
            if properties[i][1] > curMax:
                curMax = properties[i][1]
                attack = properties[i][0]
            suff.append([attack,curMax])
        suff = suff[::-1]
        # print(suff)
        def hasGreater(attack,defence,start):
            end = N-1
            while start <= end:
                mid = (start+end)//2
                if suff[mid][0] > attack and suff[mid][1] > defence:
                    return True
                elif suff[mid][0] == attack:
                    start = mid + 1
                else:
                    end = mid - 1
            return False
        ans = 0
        for j in range(N):
            if hasGreater(properties[j][0],properties[j][1],j+1):
                ans += 1
        return ans
        
        
            