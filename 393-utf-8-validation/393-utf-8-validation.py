class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def countOnes(num):
            binary = bin(num)[2:]
            diff = 8-len(binary)
            octate = "0"*diff + binary
            # print(octate)
            ones = 0
            for b in octate:
                if b == "1":
                    ones += 1
                else:
                    break
            return ones
        i = 0
        while i < len(data):
            ones = countOnes(data[i])
            if ones == 1 or ones > 4:
                return False
            if ones != 0:
                ones -= 1
                i += 1
                while ones:
                    if i >= len(data) or countOnes(data[i]) != 1:
                        return False
                    i += 1
                    ones -= 1
            else:
                i += 1
        return True
            
                    