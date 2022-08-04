class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1,n2 = (num1[::-1],num2[::-1]) if len(num1) > len(num2) else (num2[::-1],num1[::-1])
        z = 0
        ans = []
        for  i in n2:
            carry = 0
            arr = ["0"]*z
            for j in n1:
                cur = (int(i) * int(j)) + carry
                carry = cur // 10
                res = cur % 10
                arr.append(str(res))
            if carry:
                arr.append(str(carry))
            ans.append(arr[::-1])
            z += 1
        # print(ans)
        for i in range(1,len(ans)):
            ans[i] = self.add(ans[i],ans[i-1])
        # print(ans)
        return str(int("".join(ans[-1])))
    
    def add(self,num1,num2):
        n1,n2 = (num1[::-1],num2[::-1]) if len(num1) > len(num2) else (num2[::-1],num1[::-1])
        c1 = 0
        c2 = 0
        carry = 0
        ans = []
        while c1 < len(n1) and c2 < len(n2):
            cur = int(n1[c1]) + int(n2[c2]) + carry
            carry = cur // 10
            res = cur % 10
            ans.append(str(res))
            c1+=1
            c2+=1
        while c1 < len(n1):
            cur = int(n1[c1]) + carry
            carry = cur // 10
            res = cur % 10
            ans.append(str(res))
            c1+=1
            
        if carry:
            ans.append(str(carry))
        return ans[::-1]
            
            
            
            
        