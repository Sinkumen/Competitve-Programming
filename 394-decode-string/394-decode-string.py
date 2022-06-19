class Solution:
    def decodeString(self, s: str) -> str:
        word = []
        i = 0
        while i < len(s):
            if s[i].isalpha():
                word.append(s[i])
            elif s[i] == "[":
                cur = i+1
                count = 0
                while count or s[cur] != "]":
                    if s[cur] == "[":
                        count += 1
                    elif s[cur] == "]":
                        count -= 1
                    cur += 1
                res = self.decodeString(s[i+1:cur])
                temp = cur+1
                back = i-1
                multi = ""
                while back >= 0 and s[back].isdigit():
                        multi = s[back] + multi
                        back -= 1
                word.append(res*int(multi))
                i = temp
                continue
            i += 1
        return "".join(word)
            