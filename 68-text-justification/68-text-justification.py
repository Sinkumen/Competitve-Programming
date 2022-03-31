class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        i = 0
        while i < len(words):
            cur = [0,0]
            
            while i < len(words) and cur[0] + len(words[i]) <= maxWidth:
                cur.append(words[i])
                cur[0] += len(words[i])
                if cur[0] < maxWidth:
                    cur.append(" ")
                    cur[0] += 1
                    cur[1] += 1
                i += 1
            lines.append(cur)
        ans = []
        for i in range(len(lines)):
            line = lines[i]
            if line[-1] == " ":
                line.pop()
                line[0] -= 1
                line[1] -= 1
            diff = maxWidth - line[0]
            if not line[1]:
                line.append(" "*diff)
                ans.append("".join(line[2:]))
                continue
                
            each = diff//line[1] if i < len(lines)-1 else 0
            rem = diff%line[1] if i < len(lines)-1 else diff
            
            for j in range(len(line)):
                if line[j] == " ":
                    total = each
                    if rem and i < len(lines)-1 :
                        total += 1
                        rem -= 1
                    line[j] += " "*total
            if i == len(lines)-1:
                line.append(" "*rem)

            ans.append("".join(line[2:]))
                        
        return ans
                    
                    