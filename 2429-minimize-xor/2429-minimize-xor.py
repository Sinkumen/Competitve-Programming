class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1 = bin(num1)[2:]
        b2 = bin(num2)[2:]
        b1 = ("0"*(max(len(b1),len(b2)) - len(b1))) + b1
        b2 = ("0"*(max(len(b1),len(b2)) - len(b2))) + b2
        ans = ["0" for _ in range(len(b2))]
        ones = b2.count("1")
        for i in range(len(b2)):
            if b1[i] == "1" and ones:
                ans[i] = "1"
                ones -= 1
        if ones:
            for i in range(len(ans)-1,-1,-1):
                if ans[i] == "0" and ones:
                    ans[i] = "1"
                    ones -= 1
                    
        # print(ans)
        return int("".join(ans),2)