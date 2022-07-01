class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1])
        ans = 0
        while boxTypes and truckSize:
            box,size = boxTypes.pop()
            if box <= truckSize:
                truckSize -= box
                ans += (box*size)
            else:
                ans += (truckSize*size)
                truckSize -= truckSize
        return ans
                
                
            